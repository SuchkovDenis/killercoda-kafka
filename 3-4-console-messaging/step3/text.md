# Сообщения с ключами

Теперь отправим сообщения с ключами. Ключ и значение разделяются двоеточием:

`printf 'order-1:Заказ создан\norder-1:Оплата прошла\norder-2:Заказ создан\norder-1:Отправлен в доставку\norder-2:Оплата прошла\n' | docker exec -i kafka-1 /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic messages --property parse.key=true --property key.separator=:`{{exec}}

Прочитаем с отображением ключей:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --from-beginning --property print.key=true --timeout-ms 5000`{{exec}}

Обратите внимание: все сообщения с ключом `order-1` попали в одну партицию, а `order-2` — в другую.
