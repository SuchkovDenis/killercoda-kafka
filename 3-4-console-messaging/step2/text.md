# Читаем сообщения

Прочитаем все сообщения с начала топика:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --from-beginning --timeout-ms 5000`{{exec}}

Видим наши три сообщения. Флаг `--from-beginning` заставляет читать с самого начала.
