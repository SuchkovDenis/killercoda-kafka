import json
import time
from collections import defaultdict, deque
from confluent_kafka import Consumer, Producer, KafkaError

BOOTSTRAP_SERVERS = 'localhost:19092'
INPUT_TOPIC = 'transactions'
ALERTS_TOPIC = 'fraud-alerts'
GROUP_ID = 'fraud-detector'

MAX_AMOUNT_PER_10_MIN = 50000
MAX_TRANSACTIONS_PER_MIN = 10
WINDOW_10_MIN = 10 * 60
WINDOW_1_MIN = 60

user_history = defaultdict(lambda: deque())

# TODO 1: Create Consumer
consumer = None

# TODO 2: Create Producer
producer = None

def update_history(user_id, timestamp_sec, amount):
    cutoff = timestamp_sec - WINDOW_10_MIN
    history = user_history[user_id]
    while history and history[0][0] < cutoff:
        history.popleft()
    history.append((timestamp_sec, amount))

def check_high_amount(user_id):
    # TODO 3: sum amounts, compare with MAX_AMOUNT_PER_10_MIN
    return None

def check_high_frequency(user_id):
    # TODO 4: count recent transactions, compare with MAX_TRANSACTIONS_PER_MIN
    return None

def send_alert(user_id, details):
    alert = {
        'user_id': user_id,
        'rule': details['rule'],
        'details': details,
        'triggered_at': int(time.time() * 1000),
    }
    producer.produce(ALERTS_TOPIC, key=user_id, value=json.dumps(alert))
    producer.poll(0)
    print(f'  ALERT: {user_id} - {details["rule"]}')

# TODO 5: subscribe and main loop
try:
    pass
finally:
    pass
