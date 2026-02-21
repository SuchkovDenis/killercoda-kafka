# Отправляем 100 сообщений

Создайте `send_100.py`:

```python
import json, random
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:19092'})
events = ['login', 'click', 'purchase', 'logout', 'view']

for i in range(100):
    user_id = f'user-{i % 10}'
    event = random.choice(events)
    value = json.dumps({'user': user_id, 'event': event, 'seq': i})
    producer.produce('user-events', key=user_id, value=value)

producer.flush()
print('100 сообщений отправлено!')
```{{copy}}

Запустите:

`python3 /root/send_100.py`{{exec}}
