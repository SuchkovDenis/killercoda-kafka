#!/bin/bash
# Background: pull images and start Kafka cluster
echo "Pulling Docker images..."
docker pull apache/kafka:3.7.0 > /dev/null 2>&1
docker pull provectuslabs/kafka-ui:latest > /dev/null 2>&1

echo "Starting Kafka cluster..."
cd /root && docker-compose up -d 2>/dev/null

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
for i in $(seq 1 60); do
  docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list > /dev/null 2>&1 && break
  sleep 2
done

echo done > /tmp/kafka-ready
