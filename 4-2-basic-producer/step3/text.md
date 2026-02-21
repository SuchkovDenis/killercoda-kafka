# Проверка

Прочитаем сообщения через console-consumer с ключами:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning --property print.key=true --timeout-ms 5000`{{exec}}

Также можно открыть Kafka UI:

[Открыть Kafka UI]({{TRAFFIC_HOST1_8080}})

> Kafka UI может загружаться 30-60 секунд — это нормально, дождитесь появления интерфейса.

Перейдите в Topics → test-topic → Messages.
