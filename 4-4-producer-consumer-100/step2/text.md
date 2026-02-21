# Читаем и анализируем

Создайте `read_100.py`:

```python
import json
from collections import defaultdict
from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:19092',
    'group.id': 'analyzer',
    'auto.offset.reset': 'earliest',
})
consumer.subscribe(['user-events'])

by_partition = defaultdict(list)
by_user = defaultdict(list)
count = 0

try:
    while True:
        msg = consumer.poll(2.0)
        if msg is None:
            if count > 0: break
            continue
        if msg.error():
            continue
        key = msg.key().decode()
        by_partition[msg.partition()].append(key)
        by_user[key].append(msg.partition())
        count += 1
finally:
    consumer.close()

print(f'Всего прочитано: {count} сообщений\n')
print('Сообщений по партициям:')
for p in sorted(by_partition):
    print(f'  Партиция {p}: {len(by_partition[p])} сообщений')

print('\nПользователи и их партиции:')
for u in sorted(by_user):
    partitions = set(by_user[u])
    print(f'  {u}: партиция(и) {partitions} ({len(by_user[u])} сообщений)')
```{{copy}}

Запустите:

`python3 /root/read_100.py`{{exec}}
