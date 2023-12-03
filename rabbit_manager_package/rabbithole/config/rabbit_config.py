import json
from config.config_file_manager import ConfigFileManager


class RabbitConfig:
    def __init__(self, config_manager: ConfigFileManager):
        self.config_manager = config_manager
        self.config = self.load_or_initialize_config()

    def _default_config(self):
        return {
            "rabbit_server": "localhost",
            "rabbit_port": 5672,
            "rabbit_credentials": ("guest", "guest"),
            "rabbit_queues": [
                "ui_commands_queue",
                "videoreader_queue",
                "ndi_queue",
                "frame_ready_queue",
                "frame_processed_queue",
            ],
            "rabbit_exchanges": [
                {"name": "commands_exchange", "type": "fanout"},
                {"name": "frame_ready_exchange", "type": "fanout"},
                {"name": "frame_processed_exchange", "type": "fanout"},
            ],
        }

    def load_or_initialize_config(self):
        config = self.config_manager.load()
        if config is None:  # Se il file di configurazione non esiste o è vuoto
            config = self._default_config()
            config_to_save = self.__check_config(config)
            self.config_manager.save(
                config_to_save
            )  # Crea un file di configurazione di default
        else:
            return self.__check_config(config)

    def __check_config(self, config):
        default = self._default_config()

        # Assicurati che tutti i parametri necessari siano presenti
        for key in default:
            if key not in config:
                config[key] = default[key]

        # Verifica i tipi e i valori
        if not isinstance(config["rabbit_server"], str):
            raise ValueError("rabbit_server deve essere una stringa")

        if not isinstance(config["rabbit_port"], int) or config["rabbit_port"] <= 0:
            raise ValueError("rabbit_port deve essere un intero positivo")

        if not (
            isinstance(config["rabbit_credentials"], tuple)
            and len(config["rabbit_credentials"]) == 2
        ):
            raise ValueError(
                "rabbit_credentials deve essere una tupla con due elementi"
            )

        if not all(isinstance(queue, str) for queue in config["rabbit_queues"]):
            raise ValueError("Ogni elemento in rabbit_queues deve essere una stringa")

        if not all(
            isinstance(exchange, str) for exchange in config["rabbit_exchanges"]
        ):
            raise ValueError(
                "Ogni elemento in rabbit_exchanges deve essere una stringa"
            )

        return config

    def update_config(self, new_config):
        validated_config = self.__check_config(new_config)
        for key, value in validated_config.items():
            if key in self.config:
                self.config[key] = value

        self.config_file_manager.save(self.config)

    def get_config(self):
        return self.config

    def save_config(self, save_path):
        # Prima di salvare, converti il valore del font in una stringa
        save_config = self.config.copy()
        with open(save_path, "w") as config_file:
            json.dump(save_config, config_file, indent=4)
