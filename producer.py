import uuid
import json
from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for Order: {err}")
    else:
        print(f"Delivered Order ID: {msg.value().decode('utf-8')}")
        print(f"Delivered to Topic: {msg.topic()} Partition: {msg.partition()} Offset: {msg.offset()}")

order ={
    "order_id": str(uuid.uuid4()), #universally Unique identifier(UUID)
    "user":"Uday",
    "item":"mobile",
    "quantity": 5
}

key = order["order_id"].encode('utf-8')
value =json.dumps(order).encode('utf-8')

producer.produce(
    topic='orders',
    key=key, 
    value=value,
    callback=delivery_report
    )

producer.flush() # flush is used to send the order in bulk not one-by-one.

