# Проверка

Прочитаем из топика:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic crypto-prices --property print.key=true --timeout-ms 10000`{{exec}}

Откройте Kafka UI:

[Kafka UI]({{TRAFFIC_HOST1_8080}})

> Kafka UI может загружаться 30-60 секунд — это нормально, дождитесь появления интерфейса.
