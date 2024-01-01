# Welcome to Rabbit Hole’s documentation!

### *class* rabbithole.AsyncioRabbitManager(rabbit_config: [RabbitConfig](source/rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig), logger: Logger, log_level: str = 'INFO', on_message_callback=None)

The AsyncioRabbitManager class provides an asynchronous interface to connect and interact with RabbitMQ using Python and asyncio.

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

Factory for creating instances of AsyncioRabbitManager with various configurations.

This factory encapsulates the creation logic of AsyncioRabbitManager, allowing for easy customization and extension.

Example:
```python
# Create a factory instance
  factory = AsyncioRabbitManagerFactory()
  <br/>
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

### *class* rabbithole.Constants

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

### *class* rabbithole.HoleWrapper(rabbit_config: [RabbitConfig](source/rabbithole.config.md#rabbithole.config.asyncio_rabbit_config.RabbitConfig), logger: Logger, use_callback: bool = False)

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

#### *async* close_connection()
```

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

# Contents:

* [rabbithole](source/modules.md)
  * [rabbithole package](source/rabbithole.md)

# Indices and tables

* [Index](genindex.md)
* [Module Index](py-modindex.md)
* [Search Page](search.md)
