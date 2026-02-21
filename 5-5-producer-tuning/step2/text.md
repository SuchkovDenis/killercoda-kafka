# Тест при сбое брокера

Остановим один из брокеров:

`docker stop kafka-2`{{exec}}

Отправим ещё сообщения:

`python3 /root/reliable_producer.py`{{exec}}

Сообщения всё равно доставлены! Благодаря `acks=all` и репликации данные сохраняются, пока живы min.insync.replicas.

Восстановим брокер:

`docker start kafka-2`{{exec}}
