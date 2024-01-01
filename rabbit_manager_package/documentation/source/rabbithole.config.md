# rabbithole.config package

## Submodules

## rabbithole.config.asyncio_rabbit_config module

### *class* rabbithole.config.asyncio_rabbit_config.RabbitConfig(config_file_manager: ~rabbithole.config.config_file_manager.ConfigFileManager = <rabbithole.config.config_file_manager.ConfigFileManager object>, required_keys: list = [{'key': 'amqp_url', 'type': <class 'str'>}, {'key': 'sending_queue', 'type': <class 'str'>}, {'key': 'listening_queue', 'type': <class 'str'>}, {'key': 'sending_exchange', 'type': <class 'str'>}, {'key': 'reconnect_delay', 'type': <class 'int'>}, {'key': 'max_reconnect_attempts', 'type': <class 'int'>}], default_config: dict = {'amqp_url': 'amqp://guest:guest@localhost:5672/', 'listening_queue': 'my_listening_queue', 'max_reconnect_attempts': 3, 'reconnect_delay': 5, 'sending_exchange': 'my_exchange', 'sending_queue': 'my_sending_queue'})

Bases: `object`

RabbitConfig manages the configuration settings for RabbitMQ connections and interactions.
It ensures that all required configuration settings are present and correctly typed,
and provides methods to load, validate, update, and save the configuration.

Attributes:
: config_file_manager (ConfigFileManager): Manages the loading and saving of the config file.
  config (dict): A dictionary containing the current configuration settings.

#### get_config()

Retrieves the current configuration settings.

Returns:
: dict: The current configuration settings.

#### load_or_initialize_config()

Loads the configuration from a file using the ConfigFileManager. If the file does not exist or is empty,
initializes the configuration with the default settings and saves it.

Returns:
: dict: The loaded or initialized configuration.

#### save_config(save_path)

Saves the current configuration settings to a specified path.

Args:
: save_path (str): The file path where the configuration should be saved.

#### update_config(new_config)

Updates the current configuration with new settings and saves the updated configuration.

Args:
: new_config (dict): A dictionary containing the new configuration settings.

## rabbithole.config.config_file_manager module

### *class* rabbithole.config.config_file_manager.ConfigFileManager(directory, filename)

Bases: `object`

A class responsible for managing the reading and writing of configuration files.

Attributes:
: directory (str): The directory path where the configuration file is stored.
  filename (str): The name of the configuration file.

#### ensure_directory_exists()

Ensures that the directory specified exists, creating it if necessary.

#### get_full_path()

Gets the full file path of the configuration file.

Returns:
: str: The full path combining the directory and filename.

#### load()

Loads the configuration from a file. If the file doesn’t exist, returns None.

Returns:
: dict or None: The configuration loaded from the file as a dictionary, or None if the file doesn’t exist.

#### save(config)

Saves the provided configuration to a file.

Args:
: config (dict): The configuration to save.

## Module contents
