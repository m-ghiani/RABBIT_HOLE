## ConfigFileManager and RabbitConfig

### Panoramica

Le classi `ConfigFileManager` e `RabbitConfig` forniscono una struttura per gestire la configurazione di un'applicazione che interagisce con RabbitMQ. `ConfigFileManager` gestisce il salvataggio e il caricamento di configurazioni da file, mentre `RabbitConfig` utilizza `ConfigFileManager` per gestire specifiche configurazioni RabbitMQ.

### Requisiti

- Python 3.6+
- json
- os

### Utilizzo

#### ConfigFileManager

Questa classe gestisce file di configurazione in formato JSON. Permette di caricare, salvare e assicurarsi che la directory dei file di configurazione esista.

#### Esempio di Utilizzo

```python
from config_file_manager import ConfigFileManager

# Crea un'istanza di ConfigFileManager
config_manager = ConfigFileManager("config_directory", "config_file.json")

# Carica la configurazione
config = config_manager.load()

# Salva una nuova configurazione
new_config = {"chiave": "valore"}
config_manager.save(new_config)
```

#### RabbitConfig

Gestisce la configurazione specifica per RabbitMQ, caricando valori predefiniti se necessario e validando i dati.

#### Esempio di Utilizzo

```python
from rabbit_config import RabbitConfig

# Assumi che config_manager sia un'istanza di ConfigFileManager
rabbit_config = RabbitConfig(config_manager)

# Ottieni la configurazione corrente
current_config = rabbit_config.get_config()

# Aggiorna la configurazione
new_config = {"rabbit_server": "new.server.address"}
rabbit_config.update_config(new_config)

# Salva la configurazione in un percorso specifico
rabbit_config.save_config("path/to/save/config.json")
```
