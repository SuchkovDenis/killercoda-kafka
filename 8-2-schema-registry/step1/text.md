# Schema Registry

Добавьте в docker-compose и запустите Schema Registry:

`docker run -d --name schema-registry --network root_default -e SCHEMA_REGISTRY_HOST_NAME=schema-registry -e SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS=kafka-1:9092 -p 8081:8081 confluentinc/cp-schema-registry:7.6.0`{{exec}}

Проверьте:

`curl -s http://localhost:8081/subjects | python3 -m json.tool`{{exec}}
