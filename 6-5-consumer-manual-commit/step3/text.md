# Корректный коммит

Запустите `manual_consumer.py` с новой группой, которая читает и коммитит:

```python
import json
from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:19092',
    'group.id': 'correct-group',
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
    consumer.commit()
    consumer.close()
    print(f'Прочитано и закоммичено: {count}')
```{{copy}}

`python3 -c "
import json
from confluent_kafka import Consumer, KafkaError
c = Consumer({'bootstrap.servers': 'localhost:19092', 'group.id': 'correct-group', 'auto.offset.reset': 'earliest', 'enable.auto.commit': False})
c.subscribe(['batch-topic'])
count = 0
while True:
    msg = c.poll(2.0)
    if msg is None:
        if count > 0: break
        continue
    if msg.error(): continue
    count += 1
c.commit()
c.close()
print(f'Прочитано и закоммичено: {count}')
"`{{exec}}

Запустите ещё раз — 0 новых сообщений. Офсеты сохранены!
