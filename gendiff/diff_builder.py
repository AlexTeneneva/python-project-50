def deleted (key, value):
    return {
        'name' : key,
        'type' : 'deleted',
        'value' : value
    }

def added (key, value):
    return {
        'name': key,
        'type': 'added',
        'value': value
    }

def changed (key, value1, value2):
    return {
        'name' : key,
        'type' : 'changed',
        'old_value' : value1,
        'new_value' : value2
    }

def nested (key, value1, value2):
    return {
        'name': key,
        'type': 'nested',
        'value': create_diff(value1, value2)
    }

def unchanged (key, value):
    return {
        'name': key,
        'type': 'unchanged',
        'value': value
    }

def create_diff(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    result = []
    add = file2.keys() - file1.keys()
    delete = file1.keys() - file2.keys()

    for key in keys:
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key in add:
            result.append(added(key, value2))
        elif key in delete:
            result.append(deleted(key, value1))
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result.append(nested(key, value1, value2))
        elif value1 != value2:
            result.append(changed(key, value1, value2))
        else:
            result.append(unchanged(key, value1))

    sorted_diff = sorted(result, key=lambda x: x['name'])
    return sorted_diff

def build_root(file1, file2):
    return {
        'name': 'main',
        'type': 'root',
        'children': create_diff(file1, file2)
    }
