# PostgreSQL

PostgreSQL уже запущен (включён в docker-compose).

Создайте таблицу:

`docker exec -it postgres psql -U kafka -d crypto -c "CREATE TABLE IF NOT EXISTS crypto_analytics (id SERIAL PRIMARY KEY, symbol VARCHAR(20), price DECIMAL(20,8), avg_price DECIMAL(20,8), deviation_pct DECIMAL(10,4), is_anomaly BOOLEAN DEFAULT FALSE, created_at TIMESTAMP DEFAULT NOW());"`{{exec}}
