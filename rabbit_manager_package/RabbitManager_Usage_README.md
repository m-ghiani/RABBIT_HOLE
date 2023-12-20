
## RabbitManager

### Panoramica

La classe `RabbitManager` è progettata per facilitare la gestione e l'interazione con un server RabbitMQ. Offre funzionalità per configurare code e scambi, inviare e ricevere messaggi e gestire dinamicamente le risorse su RabbitMQ.

### Requisiti

- Python 3.6+
- pika
- requests

### Installazione

Assicurati di avere Python installato sul tuo sistema. È inoltre necessario installare le librerie `pika` e `requests` se non sono già presenti. Queste possono essere installate usando pip:

```bash
pip install pika requests
```

### Utilizzo

#### Inizializzazione

Per utilizzare la classe `RabbitManager`, inizializzala con i dettagli della connessione al server RabbitMQ, come il nome della coda di invio e di ascolto, lo scambio e le configurazioni specifiche:

```python
from rabbit_manager import RabbitManager
from rabbit_config import RabbitConfig

# Configurazione per RabbitMQ
rabbit_config = RabbitConfig({
    "rabbit_server": "localhost",
    "rabbit_port": 5672,
    "rabbit_credentials": ("guest", "guest")
})

rabbit_manager = RabbitManager(
    sending_queue="my_sending_queue",
    listening_queue="my_listening_queue",
    sending_exchange={"name": "my_exchange", "type": "direct"},
    config=rabbit_config
)
```

#### Connessione

Per connetterti al server RabbitMQ e configurare le code e gli scambi:

```python
rabbit_manager.connect()
```

#### Invio di Messaggi

Per inviare messaggi a una coda o a uno scambio:

```python
rabbit_manager.send_message("Il mio messaggio", to_exchange=True, routing_key="my_routing_key")
```

#### Ricezione di Messaggi

Per ascoltare i messaggi in arrivo:

```python
def my_message_callback(channel, method, properties, body):
    print("Messaggio ricevuto:", body)

rabbit_manager.on_message_callback = my_message_callback
rabbit_manager.start_listening()
```

#### Rimozione di Code o Scambi

Per rimuovere una coda o uno scambio:

```python
rabbit_manager.remove_queue("my_queue")
rabbit_manager.remove_exchange("my_exchange")
```

#### Arresto dell'Ascolto e Chiusura della Connessione

Per fermare l'ascolto dei messaggi e chiudere la connessione:

```python
rabbit_manager.stop_listening()
rabbit_manager.connection.close()
```