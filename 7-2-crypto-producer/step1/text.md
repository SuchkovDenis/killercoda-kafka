# Зависимости

`pip3 install websocket-client confluent-kafka`{{exec}}

Создайте топик:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic crypto-prices --partitions 6 --replication-factor 3`{{exec}}
