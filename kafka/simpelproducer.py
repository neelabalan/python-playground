#!/usr/bin/env python3
from kafka import KafkaProducer
from kafka.errors import KafkaError


producer = KafkaProducer(bootstrap_servers=['192.168.0.105:9092'])
if producer.bootstrap_connected():
	print ("connected to broker")
	for i in range(10) :
		future=producer.send('test', b'some_message_bytes')
	try:
		record_metadata = future.get(timeout=10)
	except KafkaError:
		pass
	print ("message published")
	print (record_metadata.topic)
	print (record_metadata.partition)
	print (record_metadata.offset)
else:
	print("connection not good")
