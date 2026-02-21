# Producer с ключами

Создайте `producer_keys.py`:

```python
import json
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:19092'})

orders = [
    ('order-1', {'status': 'created', 'item': 'Laptop'}),
    ('order-1', {'status': 'paid', 'amount': 75000}),
    ('order-2', {'status': 'created', 'item': 'Phone'}),
    ('order-1', {'status': 'shipped', 'tracking': 'TR-123'}),
    ('order-2', {'status': 'paid', 'amount': 45000}),
]

for key, value in orders:
    producer.produce(
        topic='test-topic',
        key=key,
        value=json.dumps(value),
        callback=lambda err, msg: print(
            f'  {msg.key().decode()}: partition={msg.partition()} offset={msg.offset()}'
        ) if not err else print(f'Ошибка: {err}'),
    )

producer.flush()
print('Заказы отправлены!')
```{{copy}}

Запустите:

`python3 /root/producer_keys.py`{{exec}}

Обратите внимание: все сообщения `order-1` попали в одну партицию, `order-2` — в другую.
