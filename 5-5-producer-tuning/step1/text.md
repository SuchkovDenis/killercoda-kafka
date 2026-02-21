# Надёжный Producer

Создайте `reliable_producer.py` с боевыми настройками:

```python
import json, time
from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:19092',
    'acks': 'all',
    'enable.idempotence': True,
    'retries': 5,
    'compression.type': 'snappy',
    'linger.ms': 20,
    'batch.size': 32768,
})

start = time.time()
for i in range(1000):
    producer.produce('tuning-test', key=f'key-{i%10}', value=json.dumps({'seq': i, 'data': 'x' * 100}))
    producer.poll(0)
producer.flush()
elapsed = time.time() - start
print(f'1000 сообщений за {elapsed:.2f} сек ({1000/elapsed:.0f} msg/sec)')
```{{copy}}

`python3 /root/reliable_producer.py`{{exec}}
