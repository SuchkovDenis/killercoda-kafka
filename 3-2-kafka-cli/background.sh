#!/bin/bash
cat > /tmp/wait-kafka.sh << 'WAITSCRIPT'
clear
cat <<'EOF'

=============================================
  Kafka-кластер загружается...
=============================================

  Скачиваются Docker-образы и запускается кластер.
  Обычно это занимает 1-3 минуты.
  Пока ждёте — читайте инструкцию справа.

EOF
while [ ! -f /tmp/kafka-ready ]; do printf "\r  ⏳ Ожидаем готовности..."; sleep 0.5; done
cat <<'EOF'


=============================================
  ✅ Kafka-кластер готов!
=============================================

  Можно приступать к заданию.

EOF
WAITSCRIPT
cp /root/assets/docker-compose.yml /root/docker-compose.yml
docker pull apache/kafka:3.7.0 > /dev/null 2>&1
docker pull provectuslabs/kafka-ui:latest > /dev/null 2>&1
cd /root && docker-compose up -d 2>/dev/null
for i in $(seq 1 60); do
  docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list > /dev/null 2>&1 && break
  sleep 2
done
echo done > /tmp/kafka-ready
