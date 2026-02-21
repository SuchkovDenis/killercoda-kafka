# Полная инфраструктура

Весь стек уже запущен: Kafka + PostgreSQL + Kafka UI.

Создаём топик и таблицу:

`docker exec kafka-1 /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic crypto-prices --partitions 6 --replication-factor 3 2>/dev/null`{{exec}}

`docker exec postgres psql -U kafka -d crypto -c "CREATE TABLE IF NOT EXISTS crypto_analytics (id SERIAL PRIMARY KEY, symbol VARCHAR(20), price DECIMAL(20,8), avg_price DECIMAL(20,8), deviation_pct DECIMAL(10,4), is_anomaly BOOLEAN DEFAULT FALSE, created_at TIMESTAMP DEFAULT NOW());"`{{exec}}
