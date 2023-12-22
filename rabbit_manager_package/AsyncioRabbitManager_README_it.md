
# AsyncioRabbitManager

La classe `AsyncioRabbitManager` offre un'interfaccia asincrona per connettersi e interagire con RabbitMQ utilizzando Python e asyncio. Progettata per applicazioni che richiedono elaborazione reattiva e non bloccante, questa classe gestisce la connessione a RabbitMQ, l'invio e la ricezione di messaggi, e la dichiarazione di scambi e code, tutto in modo asincrono.

## Caratteristiche Principali

- **Connessione Asincrona:** Stabilisce connessioni non bloccanti a RabbitMQ, permettendo al resto dell'applicazione di continuare l'esecuzione mentre gestisce le operazioni di rete in background.
- **Gestione dei Canali:** Apertura e configurazione dei canali RabbitMQ per inviare e ricevere messaggi.
- **Invio e Ricezione di Messaggi:** Supporta l'invio di messaggi a code o scambi e la configurazione di callback asincroni per la gestione di messaggi in arrivo.
- **Integrazione con Asyncio:** Costruita attorno alle primitive di asyncio, facilita l'integrazione con altre operazioni asincrone e il ciclo degli eventi.
- **Logging Avanzato:** Utilizza un sistema di logging personalizzabile per monitorare le attività e diagnosticare rapidamente eventuali problemi.

## Utilizzo

Ideale per applicazioni basate su asyncio che richiedono una comunicazione efficace e asincrona con RabbitMQ. Particolarmente utile in contesti in cui le prestazioni e la reattività sono critiche, come nei microservizi, nei bot, o in sistemi di elaborazione di dati in tempo reale.

### Inizializzazione

```python
import logging
from tuo_modulo import AsyncioRabbitManager  # Sostituisci con il nome effettivo del tuo modulo

logger = logging.getLogger(__name__)

rabbit_manager = AsyncioRabbitManager(
    amqp_url="il_tuo_url_amqp",
    sending_queue="la_tua_coda_di_invio",
    listening_queue="la_tua_coda_di_ascolto",
    sending_exchange="il_tuo_scambio_di_invio",
    logger=logger,
    on_message_callback=la_tua_funzione_di_callback_dei_messaggi  # Sostituisci con la tua funzione di callback
)
```

### Connessione a RabbitMQ

```python
import asyncio

async def main():
    await rabbit_manager.connect()

asyncio.run(main())
```

### Invio di Messaggi

```python
message = {"chiave": "valore"}  # Il contenuto del tuo messaggio
routing_key = "la_tua_chiave_di_routing"  # Opzionale
to_exchange = False  # Imposta su True se si invia a uno scambio

rabbit_manager.send_message(message, routing_key, to_exchange)
```

### Ricezione di Messaggi

Implementa la logica di gestione dei messaggi in una funzione di callback:

```python
async def gestore_messaggi(channel, method, properties, body):
    print("Messaggio ricevuto:", body)

# Imposta questa come la tua funzione di callback
rabbit_manager.on_message_callback = gestore_messaggi
```

### Chiusura della Connessione

```python
async def close():
    await rabbit_manager.close_connection()

asyncio.run(chiudi())
```

## Installazione

Assicurati di avere installato `pika` e `asyncio`:

```shell
pip install pika asyncio
```

## Licenza

Specifica la tua licenza o dichiara che il progetto è senza licenza.

---

Questo README fornisce una panoramica di base ed esempi per la classe `AsyncioRabbitManager`. Regola il contenuto per adattarlo alle specifiche della tua implementazione e dell'ambiente.
