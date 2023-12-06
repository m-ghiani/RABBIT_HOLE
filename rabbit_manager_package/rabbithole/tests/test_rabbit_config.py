import pytest
from rabbithole.config import RabbitConfig
from rabbithole.config import ConfigFileManager


# Definisci una fixture per creare un oggetto ConfigFileManager temporaneo
@pytest.fixture
def config_manager(tmp_path):
    directory = tmp_path / "test_config"
    filename = "test_config.json"
    return ConfigFileManager(str(directory), filename)


@pytest.fixture
def rabbit_config(config_manager):
    return RabbitConfig(config_manager)


def test_default_config_loaded(rabbit_config):
    # Verifica che la configurazione di default venga caricata correttamente
    print(rabbit_config)
    print(rabbit_config.config)
    assert rabbit_config.config["rabbit_server"] == "localhost"


def test_invalid_config_raises_exception(config_manager):
    # Crea un file di configurazione invalido
    invalid_config = {"rabbit_server": 123, "rabbit_port": "not_an_int"}
    config_manager.save(invalid_config)

    # Verifica che il caricamento di una configurazione non valida sollevi un'eccezione
    with pytest.raises(ValueError):
        RabbitConfig(config_manager)


def test_update_config_updates_values(rabbit_config):
    new_config_part = {"rabbit_server": "new.server.address"}
    rabbit_config.update_config(new_config_part)
    assert rabbit_config.config["rabbit_server"] == "new.server.address"
