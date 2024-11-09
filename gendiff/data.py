import json
#import yaml
import os

def extract_data(path):
	with open(path, encoding='utf8') as file:
		data = file.read()
		_, format = os.path.splitext(path)
	return data, format

def get_data(data, format):
	if format =='.json':
		return json.load(open('data'))
	elif format == '.yml' or format=='yaml':
		return yaml.safe_load(data)
	else:
		return "Not found such extension"
