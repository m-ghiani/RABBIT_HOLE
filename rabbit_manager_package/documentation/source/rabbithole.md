# rabbithole package

## Subpackages

* [rabbithole.config package](rabbithole.config.md)
  * [Submodules](rabbithole.config.md#submodules)
  * [rabbithole.config.asyncio_rabbit_config module](rabbithole.config.md#module-rabbithole.config.asyncio_rabbit_config)
    * [`RabbitConfig`](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig)
      * [`RabbitConfig.get_config()`](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig.get_config)
      * [`RabbitConfig.load_or_initialize_config()`](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig.load_or_initialize_config)
      * [`RabbitConfig.save_config()`](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig.save_config)
      * [`RabbitConfig.update_config()`](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig.update_config)
  * [rabbithole.config.config_file_manager module](rabbithole.config.md#module-rabbithole.config.config_file_manager)
    * [`ConfigFileManager`](rabbithole.config.md#rabbithole.config.config_file_manager.ConfigFileManager)
      * [`ConfigFileManager.ensure_directory_exists()`](rabbithole.config.md#rabbithole.config.config_file_manager.ConfigFileManager.ensure_directory_exists)
      * [`ConfigFileManager.get_full_path()`](rabbithole.config.md#rabbithole.config.config_file_manager.ConfigFileManager.get_full_path)
      * [`ConfigFileManager.load()`](rabbithole.config.md#rabbithole.config.config_file_manager.ConfigFileManager.load)
      * [`ConfigFileManager.save()`](rabbithole.config.md#rabbithole.config.config_file_manager.ConfigFileManager.save)
  * [Module contents](rabbithole.config.md#module-rabbithole.config)

## Submodules

## rabbithole.asyncio_rabbit_manager module

### *class* rabbithole.asyncio_rabbit_manager.AsyncioRabbitManager(rabbit_config: [RabbitConfig](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig), logger: Logger, log_level: str = 'INFO', on_message_callback=None)

Bases: `object`

The AsyncioRabbitManager class provides an asynchronous interface to connect and interact with RabbitMQ using Python and asyncio.

#### *async* attempt_reconnect()

#### *async* close_connection()

Closes the connection with RabbitMQ asynchronously.

#### *async* close_resources()

Chiude delicatamente il canale e la connessione.

#### *async* connect()

Establishes an asynchronous connection with RabbitMQ and prepares the channel and exchange.

#### send_message(message, routing_key='', to_exchange=False)

Sends a message to RabbitMQ.

Args:
: message: The message to send.
  routing_key (str, optional): Routing key for the message.
  to_exchange (bool, optional): Whether to send the message to the exchange.

## rabbithole.asyncio_rabbit_manager_factory module

### *class* rabbithole.asyncio_rabbit_manager_factory.AsyncioRabbitManagerFactory

Bases: `object`

Factory for creating instances of AsyncioRabbitManager with various configurations.

This factory encapsulates the creation logic of AsyncioRabbitManager, allowing for easy customization and extension.

Example:
```python
 # Create a factory instance
  factory = AsyncioRabbitManagerFactory()

  # Use the factory to create an AsyncioRabbitManager instance
  rabbit_manager = factory.create(rabbit_config, logger, callback)
```
#### create(config_file_name, config_directory: str = 'app_config', sending_queue: str = '', listening_queue: str = '', sending_exchange: str = '', log_level: str = 'INFO', on_message_callback=None)

Creates and returns an instance of AsyncioRabbitManager.

* **Parameters:**
  * **rabbit_config** – The configuration settings for RabbitMQ.
  * **logger** – The logger instance to be used by the manager.
  * **on_message_callback** – Optional callback for incoming messages.
* **Returns:**
  An instance of AsyncioRabbitManager.

## rabbithole.constants module

### *class* rabbithole.constants.Constants

Bases: `object`

Constants class contains a set of constant values used for logging messages
throughout the application, particularly in the context of managing
connections and channels with RabbitMQ.

#### ATTEMPT_RECONNECT *= 'Attempt to reconnect {}/{} in {} seconds...'*

Message indicating an attempt to reconnect to RabbitMQ, showing the attempt number, total attempts, and wait time.

#### CHANNEL_CLOSED *= 'RabbitMQ channel closed.'*

Indicates that a RabbitMQ channel has been closed.

#### CHANNEL_CLOSING_ERROR *= 'Error in closing channel: {}'*

Error message when there’s an issue closing a channel.

#### CHANNEL_NOT_OPENED *= 'Channel not opened'*

Indicates that a channel was not opened when expected.

#### CHANNEL_OPENED *= 'Channel opened'*

Indicates that a channel has been successfully opened.

#### CHANNEL_OPENED_DEBUG *= 'Channel opened: {}'*

Provides detailed debug information when a channel is opened.

#### CHANNEL_OPEN_ERROR *= 'Error in opening channel: {}'*

Specific error message when there’s an issue opening a channel.

#### CHANNEL_OPEN_ERROR_DEBUG *= 'Channel {} open error: {}'*

Detailed debug information for a channel open error.

#### CHANNEL_OPEN_FAILED *= 'Failed to open channel: {}'*

Indicates a failure to open a channel, with details.

#### CONNECTION_CLOSED *= 'Connection closed: {}'*

Indicates that a connection has been closed, with details.

#### CONNECTION_CLOSED_DEBUG *= 'Connection closed: {}'*

Provides detailed debug information when a connection is closed.

#### CONNECTION_CLOSING_ERROR *= 'Error in closing connection: {}'*

Error message when there’s an issue closing a connection.

#### CONNECTION_FAILED *= 'Failed to connect to RabbitMQ: {}'*

Indicates a failure to connect to RabbitMQ, with details.

#### CONNECTION_NOT_ESTABLISHED *= 'Connection not established'*

Indicates that a connection has not been established.

#### CONNECTION_NOT_OPENED *= 'Connection not opened'*

Indicates that a connection was not opened when expected.

#### CONNECTION_NOT_OPEN_ERROR *= 'Connection not open'*

Error message indicating that an operation was attempted on a connection that isn’t open.

#### CONNECTION_OPENED *= 'Connection opened'*

Indicates that a connection has been successfully opened.

#### CONNECTION_OPENED_DEBUG *= 'Connection opened: {}'*

Provides detailed debug information when a connection is opened.

#### CONNECTION_OPEN_ERROR *= 'Connection open error: {}'*

Specific error message when there’s an issue opening a connection.

#### CONNECTION_OPEN_ERROR_DEBUG *= 'Connection {} open error: {}'*

Detailed debug information for a connection open error.

#### ERROR_CALLBACK_NOT_ASYNC *= 'on_event_callback is not set correctly or is not asynchronous.'*

Error message indicating that the event callback is not set up correctly or is not asynchronous.

#### ERROR_CALLBACK_NOT_ASYNC_PROVIDED *= 'The provided callback is not asynchronous.'*

Error message indicating that the provided callback is not asynchronous.

#### ERROR_EXECUTION_CALLBACK *= 'Error during the execution of on_event_callback: {}'*

Error message for issues during the execution of an event callback.

#### ERROR_STACK_TRACE *= 'Details of the stack trace: {}'*

Provides details of a stack trace when an error occurs.

#### GENERIC_ERROR *= 'Error: {}'*

Generic error message with a placeholder for additional details.

#### MAX_RECONNECT_ATTEMPTS_REACHED *= 'Reached the maximum number of reconnection attempts ({}).'*

Indicates that the maximum number of reconnection attempts has been reached (similar to RECONNECT_FAILED).

#### MESSAGE_PROCESSING_ERROR *= 'Error while processing message: {}'*

Error message when there’s an issue processing a message.

#### MESSAGE_PROCESSING_ERROR_DEBUG *= 'Error while processing message: {} on channel: {}, method: {}, properties: {}, error: {}'*

Provides detailed debug information for a message processing error.

#### MESSAGE_RECEIVED *= 'Received message: {} on channel: {}'*

Message indicating that a message has been received on a specific channel.

#### MESSAGE_RECEIVED_DEBUG *= 'Received message: {} on channel: {}, method: {}, properties: {}'*

Provides detailed debug information when a message is received.

#### MESSAGE_SENDING_ERROR *= 'Error while sending message: {}'*

Error message when there’s an issue sending a message.

#### MESSAGE_SENDING_ERROR_DEBUG *= 'Error while sending message: {} on channel: {}, error: {}'*

Provides detailed debug information for a message sending error.

#### MESSAGE_SEND_FAILED *= 'Failed to send message: {}'*

Indicates that a message failed to be sent.

#### MESSAGE_SENT *= 'Message sent to {}: {}'*

Indicates that a message has been sent to a specific destination.

#### QUEUE_DECLARED *= '[x] {} declared'*

Message indicating that a queue has been declared, with the queue name.

#### QUEUE_DECLARED_DEBUG *= '[x] {} declared: {}'*

Provides detailed debug information when a queue is declared.

#### RECONNECT_FAILED *= 'Reached the maximum number of reconnection attempts ({}).'*

Message indicating that the maximum number of reconnection attempts has been reached.

#### START_CONSUMING *= '{}: Start consuming on {}'*

Indicates the start of message consumption on a specified queue.

#### START_CONSUMING_NO_QUEUE *= '{}: No listening queue declared'*

Indicates an attempt to start consuming without a declared queue.

## rabbithole.hole_wrapper module

### *class* rabbithole.hole_wrapper.HoleWrapper(rabbit_config: [RabbitConfig](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig), logger: Logger, use_callback: bool = False)

Bases: `object`

RabbitHoleManager manages the connection and communication with a RabbitMQ server.
It provides methods to connect, send messages, and handle incoming messages with optional asynchronous callbacks.

Attributes:
rabbit_config (RabbitConfig): Configuration settings for RabbitMQ.
logger (Logger): Logger for recording messages and errors.
rabbit_manager (AsyncioRabbitManager): The manager handling the RabbitMQ operations.
on_event_callback (Callable): Asynchronous callback function for incoming messages.

Example:
```python
# Initialize the manager with proper configuration and logger
manager = RabbitHoleManager(rabbit_config, logger, use_callback=True)

# Define an asynchronous callback function
async def my_callback(channel, method, properties, body):

> print(“Received message: “, body)

# Set the callback function
manager.set_on_event_callback(my_callback)

# Connect to the RabbitMQ server
await manager.connect()

# Send a message
manager.send_message(‘Hello, World!’)

# Close the connection
await manager.close_connection()
```

#### *async* close_connection()

Asynchronously close the connection to the RabbitMQ server.

#### *async* connect()

Asynchronously connect to the RabbitMQ server.

#### *async* on_message_callback(channel, method, properties, body)

Asynchronous callback for processing messages from RabbitMQ.

* **Parameters:**
  * **channel** – The channel object.
  * **method** – The method frame.
  * **properties** – The properties frame.
  * **body** – The message body.

#### send_message(message)

Send a message to the RabbitMQ server.

* **Parameters:**
  **message** – The message to be sent.

#### set_on_event_callback(callback: Callable)

Set the callback function for handling events, verifying that it’s an asynchronous function.

* **Parameters:**
  **callback** – The callback function to be set.

## Module contents

### *class* rabbithole.AsyncioRabbitManager(rabbit_config: [RabbitConfig](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig), logger: Logger, log_level: str = 'INFO', on_message_callback=None)

Bases: `object`

The AsyncioRabbitManager class provides an asynchronous interface to connect and interact with RabbitMQ using Python and asyncio.

#### *async* attempt_reconnect()

#### *async* close_connection()

Closes the connection with RabbitMQ asynchronously.

#### *async* close_resources()

Chiude delicatamente il canale e la connessione.

#### *async* connect()

Establishes an asynchronous connection with RabbitMQ and prepares the channel and exchange.

#### send_message(message, routing_key='', to_exchange=False)

Sends a message to RabbitMQ.

Args:
: message: The message to send.
  routing_key (str, optional): Routing key for the message.
  to_exchange (bool, optional): Whether to send the message to the exchange.

### *class* rabbithole.AsyncioRabbitManagerFactory

Bases: `object`

Factory for creating instances of AsyncioRabbitManager with various configurations.

This factory encapsulates the creation logic of AsyncioRabbitManager, allowing for easy customization and extension.

Example:
```python
# Create a factory instance
  factory = AsyncioRabbitManagerFactory()

  # Use the factory to create an AsyncioRabbitManager instance
  rabbit_manager = factory.create(rabbit_config, logger, callback)
```
#### create(config_file_name, config_directory: str = 'app_config', sending_queue: str = '', listening_queue: str = '', sending_exchange: str = '', log_level: str = 'INFO', on_message_callback=None)

Creates and returns an instance of AsyncioRabbitManager.

* **Parameters:**
  * **rabbit_config** – The configuration settings for RabbitMQ.
  * **logger** – The logger instance to be used by the manager.
  * **on_message_callback** – Optional callback for incoming messages.
* **Returns:**
  An instance of AsyncioRabbitManager.

### *class* rabbithole.ConfigFileManager(directory, filename)

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

### *class* rabbithole.Constants

Bases: `object`

Constants class contains a set of constant values used for logging messages
throughout the application, particularly in the context of managing
connections and channels with RabbitMQ.

#### ATTEMPT_RECONNECT *= 'Attempt to reconnect {}/{} in {} seconds...'*

Message indicating an attempt to reconnect to RabbitMQ, showing the attempt number, total attempts, and wait time.

#### CHANNEL_CLOSED *= 'RabbitMQ channel closed.'*

Indicates that a RabbitMQ channel has been closed.

#### CHANNEL_CLOSING_ERROR *= 'Error in closing channel: {}'*

Error message when there’s an issue closing a channel.

#### CHANNEL_NOT_OPENED *= 'Channel not opened'*

Indicates that a channel was not opened when expected.

#### CHANNEL_OPENED *= 'Channel opened'*

Indicates that a channel has been successfully opened.

#### CHANNEL_OPENED_DEBUG *= 'Channel opened: {}'*

Provides detailed debug information when a channel is opened.

#### CHANNEL_OPEN_ERROR *= 'Error in opening channel: {}'*

Specific error message when there’s an issue opening a channel.

#### CHANNEL_OPEN_ERROR_DEBUG *= 'Channel {} open error: {}'*

Detailed debug information for a channel open error.

#### CHANNEL_OPEN_FAILED *= 'Failed to open channel: {}'*

Indicates a failure to open a channel, with details.

#### CONNECTION_CLOSED *= 'Connection closed: {}'*

Indicates that a connection has been closed, with details.

#### CONNECTION_CLOSED_DEBUG *= 'Connection closed: {}'*

Provides detailed debug information when a connection is closed.

#### CONNECTION_CLOSING_ERROR *= 'Error in closing connection: {}'*

Error message when there’s an issue closing a connection.

#### CONNECTION_FAILED *= 'Failed to connect to RabbitMQ: {}'*

Indicates a failure to connect to RabbitMQ, with details.

#### CONNECTION_NOT_ESTABLISHED *= 'Connection not established'*

Indicates that a connection has not been established.

#### CONNECTION_NOT_OPENED *= 'Connection not opened'*

Indicates that a connection was not opened when expected.

#### CONNECTION_NOT_OPEN_ERROR *= 'Connection not open'*

Error message indicating that an operation was attempted on a connection that isn’t open.

#### CONNECTION_OPENED *= 'Connection opened'*

Indicates that a connection has been successfully opened.

#### CONNECTION_OPENED_DEBUG *= 'Connection opened: {}'*

Provides detailed debug information when a connection is opened.

#### CONNECTION_OPEN_ERROR *= 'Connection open error: {}'*

Specific error message when there’s an issue opening a connection.

#### CONNECTION_OPEN_ERROR_DEBUG *= 'Connection {} open error: {}'*

Detailed debug information for a connection open error.

#### ERROR_CALLBACK_NOT_ASYNC *= 'on_event_callback is not set correctly or is not asynchronous.'*

Error message indicating that the event callback is not set up correctly or is not asynchronous.

#### ERROR_CALLBACK_NOT_ASYNC_PROVIDED *= 'The provided callback is not asynchronous.'*

Error message indicating that the provided callback is not asynchronous.

#### ERROR_EXECUTION_CALLBACK *= 'Error during the execution of on_event_callback: {}'*

Error message for issues during the execution of an event callback.

#### ERROR_STACK_TRACE *= 'Details of the stack trace: {}'*

Provides details of a stack trace when an error occurs.

#### GENERIC_ERROR *= 'Error: {}'*

Generic error message with a placeholder for additional details.

#### MAX_RECONNECT_ATTEMPTS_REACHED *= 'Reached the maximum number of reconnection attempts ({}).'*

Indicates that the maximum number of reconnection attempts has been reached (similar to RECONNECT_FAILED).

#### MESSAGE_PROCESSING_ERROR *= 'Error while processing message: {}'*

Error message when there’s an issue processing a message.

#### MESSAGE_PROCESSING_ERROR_DEBUG *= 'Error while processing message: {} on channel: {}, method: {}, properties: {}, error: {}'*

Provides detailed debug information for a message processing error.

#### MESSAGE_RECEIVED *= 'Received message: {} on channel: {}'*

Message indicating that a message has been received on a specific channel.

#### MESSAGE_RECEIVED_DEBUG *= 'Received message: {} on channel: {}, method: {}, properties: {}'*

Provides detailed debug information when a message is received.

#### MESSAGE_SENDING_ERROR *= 'Error while sending message: {}'*

Error message when there’s an issue sending a message.

#### MESSAGE_SENDING_ERROR_DEBUG *= 'Error while sending message: {} on channel: {}, error: {}'*

Provides detailed debug information for a message sending error.

#### MESSAGE_SEND_FAILED *= 'Failed to send message: {}'*

Indicates that a message failed to be sent.

#### MESSAGE_SENT *= 'Message sent to {}: {}'*

Indicates that a message has been sent to a specific destination.

#### QUEUE_DECLARED *= '[x] {} declared'*

Message indicating that a queue has been declared, with the queue name.

#### QUEUE_DECLARED_DEBUG *= '[x] {} declared: {}'*

Provides detailed debug information when a queue is declared.

#### RECONNECT_FAILED *= 'Reached the maximum number of reconnection attempts ({}).'*

Message indicating that the maximum number of reconnection attempts has been reached.

#### START_CONSUMING *= '{}: Start consuming on {}'*

Indicates the start of message consumption on a specified queue.

#### START_CONSUMING_NO_QUEUE *= '{}: No listening queue declared'*

Indicates an attempt to start consuming without a declared queue.

### *class* rabbithole.HoleWrapper(rabbit_config: [RabbitConfig](rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig), logger: Logger, use_callback: bool = False)

Bases: `object`

RabbitHoleManager manages the connection and communication with a RabbitMQ server.
It provides methods to connect, send messages, and handle incoming messages with optional asynchronous callbacks.

Attributes:
rabbit_config (RabbitConfig): Configuration settings for RabbitMQ.
logger (Logger): Logger for recording messages and errors.
rabbit_manager (AsyncioRabbitManager): The manager handling the RabbitMQ operations.
on_event_callback (Callable): Asynchronous callback function for incoming messages.

Example:
```python
# Initialize the manager with proper configuration and logger
manager = RabbitHoleManager(rabbit_config, logger, use_callback=True)

# Define an asynchronous callback function
async def my_callback(channel, method, properties, body):

> print(“Received message: “, body)

# Set the callback function
manager.set_on_event_callback(my_callback)

# Connect to the RabbitMQ server
await manager.connect()

# Send a message
manager.send_message(‘Hello, World!’)

# Close the connection
await manager.close_connection()
```

#### *async* close_connection()

Asynchronously close the connection to the RabbitMQ server.

#### *async* connect()

Asynchronously connect to the RabbitMQ server.

#### *async* on_message_callback(channel, method, properties, body)

Asynchronous callback for processing messages from RabbitMQ.

* **Parameters:**
  * **channel** – The channel object.
  * **method** – The method frame.
  * **properties** – The properties frame.
  * **body** – The message body.

#### send_message(message)

Send a message to the RabbitMQ server.

* **Parameters:**
  **message** – The message to be sent.

#### set_on_event_callback(callback: Callable)

Set the callback function for handling events, verifying that it’s an asynchronous function.

* **Parameters:**
  **callback** – The callback function to be set.

### *class* rabbithole.RabbitConfig(config_file_manager: rabbithole.config.config_file_manager.ConfigFileManager = <rabbithole.config.config_file_manager.ConfigFileManager object>, required_keys: list = [{'key': 'amqp_url', 'type': <class 'str'>}, {'key': 'sending_queue', 'type': <class 'str'>}, {'key': 'listening_queue', 'type': <class 'str'>}, {'key': 'sending_exchange', 'type': <class 'str'>}, {'key': 'reconnect_delay', 'type': <class 'int'>}, {'key': 'max_reconnect_attempts', 'type': <class 'int'>}], default_config: dict = {'amqp_url': 'amqp://guest:guest@localhost:5672/', 'listening_queue': 'my_listening_queue', 'max_reconnect_attempts': 3, 'reconnect_delay': 5, 'sending_exchange': 'my_exchange', 'sending_queue': 'my_sending_queue'})

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
