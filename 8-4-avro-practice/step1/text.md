# Avro-схема

Создайте файл `order.avsc`:

```json
{
  "type": "record",
  "name": "Order",
  "namespace": "com.example",
  "fields": [
    {"name": "id", "type": "string"},
    {"name": "amount", "type": "double"},
    {"name": "status", "type": "string"}
  ]
}
```{{copy}}

`pip3 install confluent-kafka[avro] requests`{{exec}}
