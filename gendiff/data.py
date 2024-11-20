import json
#import yaml


def get_data(path):
	with open(path, encoding='utf8'):
		if path.endswith('.json'):
			return json.load(open(path))
		elif path.endswith('.yml') or path.endswith('.yaml'):
			return yaml.safe_load(path)
		else:
			return "Not found such extension"
