# Producer без ключа

Создайте файл `producer.py`:

```python
import json
from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:19092',
})

def delivery_callback(err, msg):
    if err:
        print(f'Ошибка: {err}')
    else:
        print(f'Доставлено: partition={msg.partition()} offset={msg.offset()}')

for i in range(5):
    producer.produce(
        topic='test-topic',
        value=f'Сообщение {i}'.encode('utf-8'),
        callback=delivery_callback,
    )

producer.flush()
print('Все сообщения отправлены!')
```{{copy}}

Запустите:

`python3 /root/producer.py`{{exec}}

Видим, что 5 сообщений распределились по разным партициям (round-robin).
