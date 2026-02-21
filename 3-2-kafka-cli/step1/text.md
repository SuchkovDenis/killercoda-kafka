# Создаём топик

Создадим топик `orders` с 3 партициями и фактором репликации 3:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic orders --partitions 3 --replication-factor 3`{{exec}}

Видим подтверждение: `Created topic orders`.
