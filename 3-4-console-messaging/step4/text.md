# Чтение из конкретной партиции

Прочитаем сообщения только из партиции 0:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --partition 0 --from-beginning --property print.key=true --timeout-ms 5000`{{exec}}

Попробуйте другие партиции (1 и 2):

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --partition 1 --from-beginning --property print.key=true --timeout-ms 5000`{{exec}}

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --partition 2 --from-beginning --property print.key=true --timeout-ms 5000`{{exec}}

Видите? Сообщения с одинаковым ключом — всегда в одной партиции.
