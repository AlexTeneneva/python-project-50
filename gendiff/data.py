import json
#import yaml
import os

def get_data(path):
	with open(path, encoding='utf8') as file:
		if path.endswith('.json'):
			return json.load(open('data'))
		elif path.endswith('.yml') or path.endswith('.yaml'):
			return yaml.safe_load(data)
		else:
			return "Not found such extension"
