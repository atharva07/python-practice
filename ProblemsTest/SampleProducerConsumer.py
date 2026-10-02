from kafka import KafkaProducer, KafkaConsumer # type: ignore
import json

# Producer 
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    # Python Objects to Bytes
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('my-topic', {'msg': "Hello, kafka"})
producer.flush()

# Consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    # Bytes to Python objects
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print(message.value)


producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('my-topic', {'msg': "Hello World"})

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers = 'localhost:9092',
    # bytes to python objects
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)