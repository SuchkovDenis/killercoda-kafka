# Отправляем сообщения

Отправим три сообщения в топик `messages` без ключей.

Каждая строка — отдельное сообщение:

`printf 'Привет, Kafka!\nВторое сообщение\nТретье сообщение\n' | docker exec -i kafka-1 /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic messages`{{exec}}

Если команда выполнилась без ошибок — сообщения записаны. В следующем шаге прочитаем их Консьюмером.
