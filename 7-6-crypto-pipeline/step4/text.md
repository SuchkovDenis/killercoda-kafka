# Аналитические запросы

`docker exec postgres psql -U kafka -d crypto -c "SELECT date_trunc('minute', created_at) AS minute, AVG(price) AS avg_price, COUNT(*) AS trades FROM crypto_analytics WHERE symbol = 'BTCUSDT' GROUP BY minute ORDER BY minute DESC LIMIT 5;"`{{exec}}

[Открыть Kafka UI]({{TRAFFIC_HOST1_8080}})

> Kafka UI может загружаться 30-60 секунд — это нормально, дождитесь появления интерфейса.
