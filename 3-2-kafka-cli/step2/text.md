# Описание и список топиков

Посмотрим детали топика:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic orders`{{exec}}

Видим информацию о каждой партиции: лидер, реплики, ISR (in-sync replicas).

Список всех топиков:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list`{{exec}}

Создадим ещё один топик для практики:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic logs --partitions 6 --replication-factor 2`{{exec}}
