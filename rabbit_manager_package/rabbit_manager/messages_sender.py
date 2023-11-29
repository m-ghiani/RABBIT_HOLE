import pika
import json


class MessagesSender:
    def __init__(self, rabbit_server, rabbit_port=5672, credentials=("guest", "guest")):
        self.rabbit_server = rabbit_server
        self.rabbit_port = rabbit_port
        self.credentials = pika.PlainCredentials(*credentials)
        self.connection_parameters = pika.ConnectionParameters(
            host=self.rabbit_server, port=self.rabbit_port, credentials=self.credentials
        )

    def connect(self):
        # Stabilire una connessione con RabbitMQ
        self.connection: pika.BlockingConnection = pika.BlockingConnection(
            self.connection_parameters
        )
        self.channel = self.connection.channel()

    def close_connection(self):
        # Chiusura della connessione
        self.connection.close()

    def add_exchanges(self, exchanges):
        # Creazione degli exchange
        print(exchanges)
        self.exchanges = exchanges
        for exchange in exchanges:
            self.channel.exchange_declare(
                exchange=exchange, exchange_type="fanout", passive=False
            )

    def send_command_to_ui(self, command, exchange):
        if not self.connection.is_open:
            self.connect()
        if exchange not in self.exchanges:
            raise ValueError("Exchange not found")

        # Invio del messaggio
        message = json.dumps(command)

        self.channel.basic_publish(exchange=exchange, routing_key="", body=message)
        print(f"Sent command to {exchange}: {message}")

        # Chiusura della connessione
