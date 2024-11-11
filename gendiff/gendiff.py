from gendiff.data import get_data

def generate_diff(file1, file2):
	file1 = get_data(file1)
	file2 = get_data(file2)
	keys = set(file1.keys() | file2.keys())
	result = []
	for key in keys:
		if file1.get(key) == file2.get(key):
			result.append(f" {key} : {file1.get(key)}")
		elif not file2.get(key):
			result.append(f"- {key} : {file1.get(key)}")
		elif not file1.get(key):
			result.append(f"+ {key} : {file2.get(key)}")
		else:
			result.append(f"- {key} : {file1.get(key)}\n+ {key} : {file2.get(key)}")
	return result
