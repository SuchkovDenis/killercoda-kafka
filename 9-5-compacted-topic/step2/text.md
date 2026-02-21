# Compaction в действии

Подождите ~10 секунд и прочитайте топик:

`sleep 10`{{exec}}

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic user-profiles --from-beginning --property print.key=true --timeout-ms 5000`{{exec}}

После compaction для user-1 останется только последнее значение (age=27).

> Compaction может занять время. Если видите все записи, подождите и перечитайте.
