import os
import pytest
from rabbithole.config import ConfigFileManager


# Definisci una fixture per creare un oggetto ConfigFileManager temporaneo
@pytest.fixture
def config_manager(tmp_path):
    directory = tmp_path / "test_config"
    filename = "test_config.json"
    return ConfigFileManager(str(directory), filename)


def test_ensure_directory_exists(config_manager):
    # Verifica che la directory sia stata creata
    assert os.path.isdir(config_manager.directory)


def test_save_and_load_config(config_manager):
    test_config = {"test_key": "test_value"}
    config_manager.save(test_config)
    loaded_config = config_manager.load()
    assert loaded_config == test_config
    assert os.path.isfile(config_manager.get_full_path())


def test_load_nonexistent_config_returns_none(config_manager):
    assert config_manager.load() is None
