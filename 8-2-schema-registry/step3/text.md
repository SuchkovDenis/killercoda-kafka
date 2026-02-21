# Совместимость

Просмотрим зарегистрированную схему:

`curl -s http://localhost:8081/subjects/orders-value/versions/1 | python3 -m json.tool`{{exec}}

Проверим совместимость новой версии:

`curl -s http://localhost:8081/config`{{exec}}
