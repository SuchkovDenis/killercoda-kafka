# Удаление и пересоздание

Удалим топик `logs`:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic logs`{{exec}}

Проверим, что он исчез:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list`{{exec}}

Создадим новый топик `events` с 4 партициями:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic events --partitions 4 --replication-factor 3`{{exec}}
