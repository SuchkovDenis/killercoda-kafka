# Consumer без auto-commit

Создайте `manual_consumer.py`:

```python
import json
from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:19092',
    'group.id': 'manual-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False,
})
consumer.subscribe(['batch-topic'])

batch = []
try:
    while True:
        msg = consumer.poll(2.0)
        if msg is None:
            if batch: break
            continue
        if msg.error(): continue
        batch.append(msg.value().decode())
        if len(batch) >= 10:
            print(f'Обработан батч из {len(batch)} сообщений')
            consumer.commit()
            print('Офсеты закоммичены!')
            batch = []
finally:
    if batch:
        print(f'Последний батч: {len(batch)} сообщений')
        consumer.commit()
    consumer.close()
```{{copy}}

`python3 /root/manual_consumer.py`{{exec}}
