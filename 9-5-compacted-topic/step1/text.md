# Compacted Topic

Создайте топик с log compaction:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic user-profiles --partitions 3 --replication-factor 3 --config cleanup.policy=compact --config min.cleanable.dirty.ratio=0.01 --config segment.ms=5000`{{exec}}

Отправьте несколько версий профиля для одного пользователя:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic user-profiles --property parse.key=true --property key.separator=: <<< "user-1:{\"name\": \"Иван\", \"age\": 25}
user-2:{\"name\": \"Мария\", \"age\": 30}
user-1:{\"name\": \"Иван\", \"age\": 26}
user-1:{\"name\": \"Иван\", \"age\": 27}"`{{exec}}
