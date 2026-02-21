# Имитация сбоя

Создайте `failing_consumer.py` — читает, но НЕ коммитит:

```python
import json
from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:19092',
    'group.id': 'fail-group',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False,
})
consumer.subscribe(['batch-topic'])

count = 0
try:
    while True:
        msg = consumer.poll(2.0)
        if msg is None:
            if count > 0: break
            continue
        if msg.error(): continue
        count += 1
finally:
    consumer.close()
    print(f'Прочитано {count} сообщений БЕЗ коммита!')
```{{copy}}

`python3 /root/failing_consumer.py`{{exec}}

Запустите ещё раз:

`python3 /root/failing_consumer.py`{{exec}}

Те же 50 сообщений! Без коммита Kafka «не знает», что мы их прочитали — at-least-once в действии.
