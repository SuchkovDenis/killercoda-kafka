# Стенд Fraud Detection

Стенд уже запущен. Создаём топики:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic transactions --partitions 6 --replication-factor 3`{{exec}}

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic fraud-alerts --partitions 3 --replication-factor 3`{{exec}}
