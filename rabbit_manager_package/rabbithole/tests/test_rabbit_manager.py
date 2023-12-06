import pytest
from unittest.mock import patch, MagicMock
from rabbit_manager import RabbitManager
from rabbithole.config import RabbitConfig, ConfigFileManager


@pytest.fixture
def rabbit_config():
    config = RabbitConfig(ConfigFileManager("test_config", "test_config.json"))
    # print(config.config)
    # config.config.rabbit_server = "localhost"
    # config.config.rabbit_port = 5672
    # config.config.rabbit_management_port = 15672
    # config.config.rabbit_credentials = ("guest", "guest")
    config.config["rabbit_queues"].append("test_queue")
    config.config["rabbit_exchanges"].append(
        {"name": "test_exchange", "type": "fanout"}
    )
    config.config["rabbit_exchanges"].append(
        {"name": "test_exchange2", "type": "fanout"}
    )

    return config.config


@pytest.fixture
def rabbit_manager(rabbit_config):
    # Creazione di mock per le dipendenze esterne come pika.
    with patch("pika.BlockingConnection") as mock_connection:
        mock_channel = MagicMock()
        mock_connection.return_value.channel.return_value = mock_channel
        return (
            RabbitManager(
                sending_queue="test_queue",
                listening_queue="test_queue",
                sending_exchange={"name": "test_exchange", "type": "fanout"},
                config=rabbit_config,
            ),
            mock_channel,
        )


@patch("pika.BlockingConnection")
def test_rabbit_connection_established(mock_connection, rabbit_config):
    RabbitManager(
        sending_queue="test_queue",
        listening_queue="test_queue",
        sending_exchange={"name": "test_exchange", "type": "fanout"},
        config=rabbit_config,
    )
    mock_connection.assert_called_once()


def test_add_queue(rabbit_manager):
    rabbit_instance, mock_channel = rabbit_manager
    rabbit_instance.add_queue("test_queue")
    mock_channel.queue_declare.assert_called_with(queue="test_queue")


def test_add_exchange(rabbit_manager):
    exchange_info = {
        "name": "test_exchange",
        "type": "direct",
        "queues": ["test_queue"],
    }
    rabbit_instance, mock_channel = rabbit_manager
    rabbit_instance.add_exchange(exchange_info)
    mock_channel.exchange_declare.assert_called_with(
        exchange="test_exchange", exchange_type="direct"
    )


def test_send_message(rabbit_manager):
    rabbit_instance, mock_channel = rabbit_manager
    rabbit_instance.send_message("test_message")
    mock_channel.basic_publish.assert_called_once()


def test_start_listening(rabbit_manager):
    rabbit_instance, mock_channel = rabbit_manager
    rabbit_instance.start_listening()
    mock_channel.basic_consume.assert_called_once()
