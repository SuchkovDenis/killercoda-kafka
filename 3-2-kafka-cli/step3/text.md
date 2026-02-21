# Изменение конфигурации

Изменим retention (срок хранения) для топика `orders` на 1 день (86400000 мс):

`docker exec kafka-1 /opt/kafka/bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name orders --add-config retention.ms=86400000`{{exec}}

Проверим, что конфигурация применилась:

`docker exec kafka-1 /opt/kafka/bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type topics --entity-name orders`{{exec}}

Видим `retention.ms=86400000` в выводе.
