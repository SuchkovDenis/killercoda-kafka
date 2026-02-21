# Проверяем работу кластера

Убедимся, что Kafka отвечает на запросы. Выполним команду внутри контейнера:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list`{{exec}}

Пустой вывод — это нормально, топиков пока нет.

Создадим тестовый топик:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic test --partitions 3 --replication-factor 3`{{exec}}

Проверим, что топик появился:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic test`{{exec}}

Видим 3 партиции, каждая с 3 репликами, распределённые по трём брокерам.
