# Producer

Запустите crypto_producer.py (из урока 7.2) в фоне:

`python3 /root/crypto_producer.py > /tmp/producer.log 2>&1 &`{{exec}}

Проверяем:

`docker exec kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic crypto-prices --timeout-ms 5000 | head -3`{{exec}}
