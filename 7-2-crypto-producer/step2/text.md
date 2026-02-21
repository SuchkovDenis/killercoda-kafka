# Crypto Producer

Создайте `crypto_producer.py` — скопируйте код из урока 7.2 на Stepik.

Основные моменты:
- Подключение к `wss://stream.binance.com:9443/stream?streams=btcusdt@trade`
- Ключ = торговая пара (BTCUSDT)
- `acks=all`, `enable.idempotence=True`

Запустите:

`python3 /root/crypto_producer.py &`{{exec}}

Остановить позже: `kill %1`{{exec}}
