import pika
import json
import requests


class RabbitManager:
    def __init__(
        self,
        sending_queues: [str],
        listening_queues: [str],
        sending_exchanges: [dict],
        config,
        on_message_callback=None,
    ):
        self.config = config
        self.rabbit_server: str = config.rabbit_server
        self.rabbit_port: int = config.rabbit_port
        self.rabbit_credentials: tuple = config.rabbit_credentials
        self.sending_queues = [
            queue for queue in sending_queues if queue in config.rabbit_queues
        ]

        self.on_message_callback = on_message_callback

        self.rabbit_connection_parameters = self._rabbit_connection_parameters()

        self.existing_queues = self.get_existing_queues()

        self.existing_exchanges = self.get_existing_exchanges()

        self.connection: pika.BlockingConnection = self._rabbit_connection()

        self.channel = self.connection.channel()

        self.listening_queues = self.setup_queues(listening_queues)

        self.sending_exchanges = self.setup_queues(sending_queues)

        self.exchanges = self.setup_exchanges(sending_exchanges)

    def _rabbit_connection_parameters(self):
        return pika.ConnectionParameters(
            host=self.rabbit_server,
            port=self.rabbit_port,
            credentials=pika.PlainCredentials(*self.rabbit_credentials),
        )

    def _rabbit_connection(self):
        return pika.BlockingConnection(self.rabbit_connection_parameters)

    def get_existing_queues(self):
        url = f"http://{self.rabbit_server}:{self.management_port}/api/queues"
        response = requests.get(url, auth=self.rabbit_credentials)
        if response.status_code == 200:
            return [queue["name"] for queue in response.json()]
        else:
            print("Unable to retrieve queues from RabbitMQ")
            return []

    def get_existing_exchanges(self):
        url = f"http://{self.rabbit_server}:{self.management_port}/api/exchanges"
        response = requests.get(url, auth=self.rabbit_credentials)
        if response.status_code == 200:
            return [exchange["name"] for exchange in response.json()]
        else:
            print("Unable to retrieve exchanges from RabbitMQ")
            return []

    def add_exchange(self, exchange_name, exchange_type="direct"):
        if exchange_name not in self.existing_exchanges:
            self.channel.exchange_declare(
                exchange=exchange_name, exchange_type=exchange_type
            )
            self._exchanges.append(exchange_name)
            print(f"Exchange {exchange_name} added")

    def remove_queue(self, queue_name):
        if queue_name in self._queues:
            self.channel.queue_delete(queue=queue_name)
            self._queues.remove(queue_name)
            print(f"Queue {queue_name} removed")

    def remove_exchange(self, exchange_name):
        if exchange_name in self._exchanges:
            self.channel.exchange_delete(exchange=exchange_name)
            self._exchanges.remove(exchange_name)
            print(f"Exchange {exchange_name} removed")

    def setup_queues(self, queues):
        return_queues = []
        for queue in queues:
            if queue not in self.existing_queues and queue in self.config.rabbit_queues:
                self.channel.queue_declare(queue=queue)
                return_queues.append(queue)
        return return_queues

    def setup_exchanges(self, exchanges: [dict]):
        return_exchanges = []
        for exchange in exchanges:
            if (
                exchange["name"] not in self.existing_exchanges
                and exchange["name"] in self.config.rabbit_exchanges
            ):
                self.channel.exchange_declare(
                    exchange=exchange["name"], exchange_type=exchange["type"]
                )
                return_exchanges.append(exchange)
        return return_exchanges

    def start_listening(self):
        self.channel.basic_consume(
            queue=self.queue, on_message_callback=self.on_message, auto_ack=True
        )
        self.channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        if self.on_message_callback:
            self.on_message_callback(ch, method, properties, body)
        else:
            print("Nessuna callback definita per il messaggio ricevuto.")

    def send_command_exchange(self, command: str, exchange: str):
        if not self.connection.is_open:
            raise ConnectionError("Connection not open")
        if exchange not in self.exchanges:
            raise ValueError("Exchange not found")

        # Invio del messaggio
        message = json.dumps(command)

        self.channel.basic_publish(exchange=exchange, routing_key="", body=message)

    def stop_listening(self):
        self.channel.stop_consuming()
        if self.connection:
            self.connection.close()
