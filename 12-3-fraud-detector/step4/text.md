# Основной цикл

**TODO 5** — замените `try: pass / finally: pass` на:
```python
consumer.subscribe([INPUT_TOPIC])
print('Fraud Detector запущен...')
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f'Ошибка: {msg.error()}')
            continue
        data = json.loads(msg.value().decode('utf-8'))
        user_id = data['user_id']
        amount = data['amount']
        ts_sec = data['timestamp'] / 1000
        update_history(user_id, ts_sec, amount)
        for check in [check_high_amount, check_high_frequency]:
            result = check(user_id)
            if result:
                send_alert(user_id, result)
finally:
    consumer.close()
    producer.flush()
```{{copy}}

Запустите (генератор должен работать):

`python3 /root/fraud_detector.py`{{exec}}

Через ~30 секунд увидите алерты!

Проверьте в Kafka UI: Topics → fraud-alerts → Messages.

[Открыть Kafka UI]({{TRAFFIC_HOST1_8080}})

> Kafka UI может загружаться 30-60 секунд — это нормально, дождитесь появления интерфейса.
