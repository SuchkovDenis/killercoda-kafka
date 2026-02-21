#!/bin/bash
docker exec kafka-1 /opt/kafka/bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type topics --entity-name orders 2>/dev/null | grep -q "retention.ms=86400000"
