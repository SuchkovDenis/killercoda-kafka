# Сравнение конфигураций

Создайте `fast_producer.py` — без idempotence, acks=1:

```python
import json, time
from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:19092',
    'acks': '1',
    'linger.ms': 50,
    'batch.size': 65536,
    'compression.type': 'lz4',
})

start = time.time()
for i in range(1000):
    producer.produce('tuning-test', key=f'key-{i%10}', value=json.dumps({'seq': i, 'data': 'x' * 100}))
    producer.poll(0)
producer.flush()
elapsed = time.time() - start
print(f'1000 сообщений за {elapsed:.2f} сек ({1000/elapsed:.0f} msg/sec)')
```{{copy}}

`python3 /root/fast_producer.py`{{exec}}

Сравните скорость: fast_producer обычно быстрее, но менее надёжен.
