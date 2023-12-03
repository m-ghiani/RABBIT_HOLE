import pika
import json
import requests


class RabbitManager:
    """
    Gestisce la connessione e l'interazione con un server RabbitMQ.

    Fornisce funzionalità per configurare code e scambi, inviare e ricevere messaggi,
    e gestire dinamicamente risorse su RabbitMQ.
    """

    def __init__(
        self,
        sending_queue: str,
        listening_queue: str,
        sending_exchange: dict,
        config,
        on_message_callback=None,
    ):
        """
        Inizializza le configurazioni della connessione RabbitMQ, le code e gli scambi.

        :param sending_queues: Liste delle code da cui inviare i messaggi.
        :param listening_queues: Liste delle code da cui ascoltare i messaggi.
        :param sending_exchanges: Liste degli scambi da cui inviare i messaggi.
        :param config: Configurazioni del server RabbitMQ.
        :param on_message_callback: Funzione callback da invocare quando viene ricevuto un messaggio.
        """
        self.config = config
        self.rabbit_server: str = config.rabbit_server
        self.rabbit_port: int = config.rabbit_port
        self.rabbit_credentials: tuple = config.rabbit_credentials

        self.on_message_callback = on_message_callback

        self.rabbit_connection_parameters = self.__rabbit_connection_parameters()

        self.existing_queues = self.get_existing_queues()

        self.existing_exchanges = self.get_existing_exchanges()

        self.connection: pika.BlockingConnection = self.__rabbit_connection()

        self.__channel = self.connection.channel()

        self.listening_queue: str = self.add_queue(listening_queue)

        self.sending_queue: str = self.add_queue(sending_queue)

        self.sending_exchange: dict = self.add_exchange(sending_exchange)

    def __rabbit_connection_parameters(self):
        return pika.ConnectionParameters(
            host=self.rabbit_server,
            port=self.rabbit_port,
            credentials=pika.PlainCredentials(*self.rabbit_credentials),
        )

    def __rabbit_connection(self):
        return pika.BlockingConnection(self.rabbit_connection_parameters)

    def get_existing_queues(self) -> list:
        url = f"http://{self.rabbit_server}:{self.management_port}/api/queues"
        response = requests.get(url, auth=self.rabbit_credentials)
        if response.status_code == 200:
            return [queue["name"] for queue in response.json()]
        else:
            print("Unable to retrieve queues from RabbitMQ")
            return []

    def get_existing_exchanges(self) -> list:
        url = f"http://{self.rabbit_server}:{self.management_port}/api/exchanges"
        response = requests.get(url, auth=self.rabbit_credentials)
        if response.status_code == 200:
            return [exchange["name"] for exchange in response.json()]
        else:
            print("Unable to retrieve exchanges from RabbitMQ")
            return []

    def remove_queue(self, queue_name):
        if queue_name in self.existing_queues:
            self.__channel.queue_delete(queue=queue_name)
            self.existing_queues.remove(queue_name)
            if queue_name == self.listening_queue:
                self.listening_queue = None
            if queue_name == self.sending_queue:
                self.sending_queue = None

    def remove_exchange(self, exchange_name):
        if exchange_name in self.existing_exchanges:
            self.__channel.exchange_delete(exchange=exchange_name)
            self.existing_exchanges.remove(exchange_name)
            if exchange_name == self.sending_exchange["name"]:
                self.sending_exchange = {}

    def add_queue(self, queue):
        if queue not in self.existing_queues and queue in self.config.rabbit_queues:
            self.__channel.queue_declare(queue=queue)
            return queue

    def __check_exchange_dict(self, exchange) -> bool:
        required_keys = {"name", "type", "queues"}
        return (
            all(key in exchange for key in required_keys)
            and isinstance(exchange["queues"], list)
            and len(exchange["queues"]) > 0
        )

    def add_exchange(self, exchange: dict) -> dict:
        if (
            self.__check_exchange_dict(exchange)
            and exchange["name"] not in self.existing_exchanges
            and exchange["name"] in self.config.rabbit_exchanges
        ):
            self.__channel.exchange_declare(
                exchange=exchange["name"], exchange_type=exchange["type"]
            )
        for queue in exchange["queues"]:
            self.add_queue(queue)
            self.__channel.queue_bind(exchange=exchange["name"], queue=queue)
        return exchange

    def start_listening(self):
        self.__channel.basic_consume(
            queue=self.listening_queue,
            on_message_callback=self.on_message,
            auto_ack=True,
        )
        self.__channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        if self.on_message_callback:
            self.on_message_callback(ch, method, properties, body)
        else:
            print("Nessuna callback definita per il messaggio ricevuto.")

    def send_message(self, message: str, to_exchange: bool = False, routing_key=""):
        if not self.connection.is_open:
            raise ConnectionError("Connection not open")

        message = json.dumps(message)

        exchange = self.sending_exchange if to_exchange else ""
        routing_key = self.sending_queue if not to_exchange else routing_key

        self.__channel.basic_publish(
            exchange=exchange, routing_key=routing_key, body=message
        )

    def stop_listening(self):
        self.__channel.stop_consuming()
        if self.connection:
            self.connection.close()
