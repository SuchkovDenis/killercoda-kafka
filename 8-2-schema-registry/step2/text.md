# Регистрация схемы

Зарегистрируем Avro-схему:

`curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" --data '{"schema": "{\"type\": \"record\", \"name\": \"Order\", \"fields\": [{\"name\": \"id\", \"type\": \"string\"}, {\"name\": \"amount\", \"type\": \"double\"}, {\"name\": \"status\", \"type\": \"string\"}]}"}' http://localhost:8081/subjects/orders-value/versions`{{exec}}

Проверяем:

`curl -s http://localhost:8081/subjects`{{exec}}
