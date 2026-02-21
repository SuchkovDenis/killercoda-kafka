# Аналитика

Проверяем данные:

`docker exec postgres psql -U kafka -d crypto -c "SELECT symbol, price, avg_price, is_anomaly FROM crypto_analytics ORDER BY created_at DESC LIMIT 10;"`{{exec}}
