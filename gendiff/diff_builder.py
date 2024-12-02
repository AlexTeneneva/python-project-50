def create_diff(file1, file2):
    keys = sorted(set(file1.keys() | file2.keys()))
    result = []
    for key in keys:
        if key not in file2.get(key):
            result[key] = {'type': 'deleted', 'value': file1[key]}
        elif type(file1[key]) == dict and type(file2[key]) == dict:
            result[key] = {'type': 'nested', 'old value': file1[key], 'new value': file2[key]}
        elif file1.get(key) != file2.get(key):
            result[key] = {'type': 'changed', 'value': file1[key]}
        elif not file1.get(key):
            result[key] = {'type': 'added', 'value': file2[key]}
        else:
            result[key] = {'type': 'unchanged', 'value': file1[key]}
