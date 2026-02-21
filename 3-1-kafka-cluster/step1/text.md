# Создаём docker-compose.yml

Давайте разберём, что будет в нашем `docker-compose.yml`. Мы поднимаем 3 брокера Kafka в режиме KRaft (без ZooKeeper) и веб-интерфейс Kafka UI.

Файл уже подготовлен. Посмотрите его содержимое:

`cat /root/assets/docker-compose.yml`{{exec}}

Ключевые параметры каждого брокера:

- **KAFKA_NODE_ID** — уникальный идентификатор (1, 2, 3)
- **KAFKA_PROCESS_ROLES: broker,controller** — каждый узел совмещает роли брокера и контроллера
- **KAFKA_CONTROLLER_QUORUM_VOTERS** — список всех контроллеров для голосования
- **CLUSTER_ID** — общий ID кластера (одинаковый у всех брокеров)
- **KAFKA_LISTENERS** — адреса, на которых брокер слушает (PLAINTEXT для внутренней связи, CONTROLLER для кворума, EXTERNAL для доступа снаружи)

Обратите внимание: у каждого брокера свой `KAFKA_NODE_ID` и свой внешний порт (19092, 19093, 19094).

Скопируйте файл в рабочую директорию:

`cp /root/assets/docker-compose.yml /root/docker-compose.yml`{{exec}}

Можете открыть файл в редакторе слева и изучить конфигурацию подробнее.
