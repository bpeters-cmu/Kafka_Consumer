from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render
from kafka import KafkaConsumer
from kafka import TopicPartition
import collections

def index(request):
    return render(request, 'client_app/index.html')

def get_coordinates(request, offset):
	consumer = KafkaConsumer()
	topic_partition = TopicPartition('Python',0)
	consumer.assign([topic_partition])			
	consumer.seek(partition = topic_partition, offset = int(offset))
	data = {}
	while not data:
		data = consumer.poll(timeout_ms = 0, max_records = 1)
	location = ''
	print(data)
	for k,v in data.items():
		location = str(v[0].value, 'utf-8')
		
	return HttpResponse(location)

def load_data(request):
	return render(request, 'client_app/dashboard.html')


