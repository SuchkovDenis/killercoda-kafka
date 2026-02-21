# Consumer и Producer

Откройте `fraud_detector.py` в редакторе слева.

**TODO 1** — замените `consumer = None` на:
```python
consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'latest',
    'enable.auto.commit': True,
})
```{{copy}}

**TODO 2** — замените `producer = None` на:
```python
producer = Producer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
})
```{{copy}}
