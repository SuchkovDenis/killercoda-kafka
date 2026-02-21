#!/bin/bash
docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic messages --from-beginning --property print.key=true --timeout-ms 3000 2>/dev/null | grep -q "order-1"
