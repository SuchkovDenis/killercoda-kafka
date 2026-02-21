# Создаём Consumer

Создайте файл `consumer.py`:

```python
import json
from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:19092',
    'group.id': 'my-first-group',
    'auto.offset.reset': 'earliest',
})

consumer.subscribe(['test-topic'])

print('Читаем сообщения...')
try:
    count = 0
    while True:
        msg = consumer.poll(timeout=2.0)
        if msg is None:
            if count > 0:
                break
            continue
        if msg.error():
            if msg.error().code() != KafkaError._PARTITION_EOF:
                print(f'Ошибка: {msg.error()}')
            continue

        key = msg.key().decode('utf-8') if msg.key() else 'null'
        value = msg.value().decode('utf-8')
        print(f'  Ключ: {key} | Значение: {value} | '
              f'Партиция: {msg.partition()} | Offset: {msg.offset()}')
        count += 1
finally:
    consumer.close()
    print(f'\nПрочитано {count} сообщений.')
```{{copy}}
