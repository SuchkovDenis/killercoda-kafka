# Повторный запуск

Запустите consumer ещё раз:

`python3 /root/consumer.py`{{exec}}

На этот раз он прочитал **0 сообщений**. Почему?

Потому что Kafka запомнила, до какого момента мы прочитали (offset был закоммичен). При повторном запуске consumer продолжает с того места, где остановился.

Чтобы убедиться, отправим новое сообщение и прочитаем:

`python3 -c "
from confluent_kafka import Producer
p = Producer({'bootstrap.servers': 'localhost:19092'})
p.produce('test-topic', key='user-new', value='Новое сообщение!')
p.flush()
print('Отправлено!')
"`{{exec}}

`python3 /root/consumer.py`{{exec}}

Теперь видим только одно новое сообщение.
