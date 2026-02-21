import json
import random
import time
import uuid
from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:19092',
    'acks': 'all',
    'enable.idempotence': True,
})

USERS = [f'user-{i}' for i in range(1, 21)]
MERCHANTS = [
    ('Ozon', 'marketplace'), ('Wildberries', 'marketplace'),
    ('Pyaterochka', 'groceries'), ('Magnit', 'groceries'),
    ('DNS', 'electronics'), ('MVideo', 'electronics'),
    ('Yandex.Taxi', 'transport'), ('Metro', 'transport'),
    ('Apteka.ru', 'pharmacy'), ('Litres', 'books'),
]
CITIES = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань']

def generate_normal_transaction(user_id):
    merchant, category = random.choice(MERCHANTS)
    return {
        'transaction_id': f'tx-{uuid.uuid4().hex[:8]}',
        'user_id': user_id,
        'amount': round(random.uniform(100, 5000), 2),
        'merchant': merchant,
        'category': category,
        'city': random.choice(CITIES),
        'timestamp': int(time.time() * 1000),
    }

def generate_suspicious_burst(user_id):
    transactions = []
    for _ in range(random.randint(12, 18)):
        merchant, category = random.choice(MERCHANTS)
        transactions.append({
            'transaction_id': f'tx-{uuid.uuid4().hex[:8]}',
            'user_id': user_id,
            'amount': round(random.uniform(50, 500), 2),
            'merchant': merchant,
            'category': category,
            'city': random.choice(CITIES),
            'timestamp': int(time.time() * 1000),
        })
    return transactions

def generate_suspicious_amount(user_id):
    transactions = []
    for _ in range(random.randint(3, 6)):
        merchant, category = random.choice(MERCHANTS)
        transactions.append({
            'transaction_id': f'tx-{uuid.uuid4().hex[:8]}',
            'user_id': user_id,
            'amount': round(random.uniform(10000, 25000), 2),
            'merchant': merchant,
            'category': category,
            'city': random.choice(CITIES),
            'timestamp': int(time.time() * 1000),
        })
    return transactions

def send(transaction):
    producer.produce(
        topic='transactions',
        key=transaction['user_id'],
        value=json.dumps(transaction),
    )
    producer.poll(0)

print('Генератор транзакций запущен.')
try:
    cycle = 0
    while True:
        for _ in range(random.randint(5, 10)):
            user = random.choice(USERS)
            tx = generate_normal_transaction(user)
            send(tx)
            print(f'  {tx["user_id"]} -> {tx["merchant"]} : {tx["amount"]} руб.')
        cycle += 1
        if cycle % 30 == 0:
            fraud_user = random.choice(USERS)
            if random.choice([True, False]):
                print(f'  ⚡ burst от {fraud_user}')
                for tx in generate_suspicious_burst(fraud_user):
                    send(tx)
            else:
                print(f'  ⚡ high_amount от {fraud_user}')
                for tx in generate_suspicious_amount(fraud_user):
                    send(tx)
        producer.flush()
        time.sleep(1)
except KeyboardInterrupt:
    producer.flush()
