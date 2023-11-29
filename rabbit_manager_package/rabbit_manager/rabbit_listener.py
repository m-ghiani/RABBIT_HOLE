import pika
import json


class RabbitListener:
    def __init__(
        self,
        queue,
        shm_name,
        rabbit_server="localhost",
        rabbit_port=5672,
        rabbit_credentials=("guest", "guest"),
        rabbit_queue="ui_commands_queue",
    ):
        self.rabbit_server: str = rabbit_server
        self.rabbit_port: int = rabbit_port
        self.rabbit_credentials: tuple = rabbit_credentials
        self.rabbit_queue: str = rabbit_queue
        self.command_queue = queue
        self.shm_name = shm_name

        self.rabbit_connection_parameters = pika.ConnectionParameters(
            host=self.rabbit_server,
            port=self.rabbit_port,
            credentials=pika.PlainCredentials(*self.rabbit_credentials),
        )
        self.rabbit_connection: pika.BlockingConnection = pika.BlockingConnection(
            self.rabbit_connection_parameters
        )
        self.rabbit_channel = self.rabbit_connection.channel()
        self.rabbit_channel.queue_declare(queue=self.rabbit_queue)

    def start_listening(self):
        self.rabbit_channel.basic_consume(
            queue=self.rabbit_queue, on_message_callback=self.on_message, auto_ack=True
        )
        self.rabbit_channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        try:
            message = json.loads(body)
            command = message.get("command", None)
            shm = message.get("shm", None)
            args = message.get("args", None)

            if command:
                print(f"Comando ricevuto: {command} per la shared memory {shm}")
                if shm == self.shm_name:
                    self.command_queue.put((command, args))
                # Qui puoi aggiungere la logica per gestire il comando
            else:
                print("Nessun comando trovato nel messaggio")
        except json.JSONDecodeError:
            print("Errore nella decodifica del messaggio JSON")
        # Qui puoi aggiungere la logica per gestire il messaggio

    def stop_listening(self):
        self.rabbit_channel.stop_consuming()
        if self.rabbit_connection:
            self.rabbit_connection.close()
