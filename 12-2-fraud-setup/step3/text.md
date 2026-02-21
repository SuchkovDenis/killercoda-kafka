# Проверка

Прочитаем из топика:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic transactions --property print.key=true --timeout-ms 10000`{{exec}}

[Открыть Kafka UI]({{TRAFFIC_HOST1_8080}})

> Kafka UI может загружаться 30-60 секунд — это нормально, дождитесь появления интерфейса.

Откройте Topics → transactions → Messages. Видим JSON-сообщения с полями user_id, amount, merchant, city.
