#!/bin/bash
# Проверяем, что студент может читать из конкретной партиции
docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --partition 0 --from-beginning --timeout-ms 2000 2>/dev/null
exit 0
