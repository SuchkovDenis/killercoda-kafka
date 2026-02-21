# Запускаем кластер

Запустите все контейнеры:

`cd /root && docker-compose up -d`{{exec}}

Первый запуск может занять несколько минут — Docker скачивает образы.

Проверьте статус контейнеров:

`docker-compose ps`{{exec}}

Все четыре сервиса (kafka-1, kafka-2, kafka-3, kafka-ui) должны быть в статусе **running**.

Если какой-то контейнер упал, посмотрите логи:

`docker-compose logs kafka-1`{{exec}}
