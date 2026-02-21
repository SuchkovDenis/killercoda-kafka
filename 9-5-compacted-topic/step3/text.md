# Tombstone

Отправьте сообщение с пустым значением (tombstone) для удаления ключа:

`echo 'user-2:' | docker exec -i kafka-1 /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic user-profiles --property parse.key=true --property key.separator=:`{{exec}}

После compaction записи user-2 исчезнут полностью.
