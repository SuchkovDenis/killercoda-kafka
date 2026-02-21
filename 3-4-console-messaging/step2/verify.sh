#!/bin/bash
# Просто проверяем, что consumer может подключиться
docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --from-beginning --timeout-ms 2000 2>/dev/null | wc -l | grep -qv "^0$"
