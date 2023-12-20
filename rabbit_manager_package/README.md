
# RabbitManager

## Panoramica

`RabbitManager` è una classe Python che facilita la gestione e l'interazione con un server RabbitMQ. Fornisce funzionalità per la configurazione di code e scambi, l'invio e la ricezione di messaggi, e la gestione dinamica delle risorse su RabbitMQ.

## Requisiti

- Python 3.6+
- pika 1.1.0+
- asyncio

## Installazione

Assicurati di avere Python installato sul tuo sistema. Inoltre, è necessario installare la libreria `pika`. Puoi installarla usando pip:

```bash
pip install pika
```

## Utilizzo

### Creazione dell'istanza `RabbitManager`

Per utilizzare la classe `RabbitManager`, è necessario prima crearne un'istanza. L'istanza richiede i dettagli della connessione al server RabbitMQ, come l'URL AMQP, il nome della coda di invio e di ascolto, e il nome dello scambio:

```python
from rabbit_manager import RabbitManager

amqp_url = 'amqp://guest:guest@localhost:5672/'
sending_queue = 'test_queue'
listening_queue = 'test_queue'
sending_exchange = 'test_exchange'

rabbit_manager = RabbitManager(amqp_url, sending_queue, listening_queue, sending_exchange)
```

### Connessione al Server RabbitMQ

Per connettersi al server RabbitMQ, usa il metodo `connect`:

```python
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(rabbit_manager.connect())
```

### Invio di Messaggi

Per inviare messaggi, utilizza il metodo `send_message`. Puoi specificare se inviare il messaggio a una coda o a uno scambio:

```python
message = {"key": "value"}
routing_key = 'test_routing_key'

loop.run_until_complete(rabbit_manager.send_message(message, routing_key=routing_key))
```

### Ricezione di Messaggi

Per ascoltare i messaggi in arrivo, assicurati di definire una callback e di avviare il processo di ascolto:

```python
def on_message_callback(channel, method, properties, body):
    print("Messaggio ricevuto:", body)

rabbit_manager.on_message_callback = on_message_callback
rabbit_manager.start_listening()
```

### Chiusura della Connessione

Per assicurare una chiusura pulita e ordinata della connessione con il server RabbitMQ, è importante chiudere correttamente la connessione e le risorse associate. La classe `RabbitManager` fornisce un metodo `close_connection` per questo scopo. Quando si chiama questo metodo, viene inviato un comando di chiusura al server RabbitMQ e vengono rilasciate tutte le risorse di rete e di sistema associate alla connessione.

È buona pratica chiudere la connessione quando il tuo programma ha finito di utilizzare RabbitMQ o sta per terminare. Questo aiuta a prevenire perdite di risorse e assicura che la coda e lo scambio non rimangano in uno stato inconsistente. Ecco come puoi chiudere la connessione:

```python
import asyncio

# Crea un'istanza della classe RabbitManager
rabbit_manager = RabbitManager(amqp_url, sending_queue, listening_queue, sending_exchange)

async def manage_rabbit():
    # Connettiti a RabbitMQ
    await rabbit_manager.connect()

    # Esegui le operazioni desiderate con RabbitMQ...

    # Chiudi la connessione quando hai finito
    await rabbit_manager.close_connection()

# Esegui la routine di gestione RabbitMQ
loop = asyncio.get_event_loop()
loop.run_until_complete(manage_rabbit())
```

Nell'esempio sopra, `manage_rabbit` è una coroutine asincrona che gestisce il ciclo di vita della connessione RabbitMQ. Dopo aver completato tutte le operazioni necessarie, chiama `rabbit_manager.close_connection()` per chiudere in modo sicuro la connessione.

Ricorda che è importante utilizzare `asyncio` per eseguire queste operazioni in quanto la classe `RabbitManager` è progettata per funzionare in modo asincrono.
