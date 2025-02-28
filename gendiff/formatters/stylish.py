def get_all_types(diff, target_key):
    types = []
    for key, value in diff.items():
        if key == target_key:
            types.append(value)
        if isinstance(value, dict):
            types.extend(get_all_types(value, target_key))
    return types



def stylish(diff: dict):
    types = get_all_types(diff, 'type')
    result = []
    indent_4 = '    '
    for key, value in diff.items():
        for type_value in types:
            match type_value:
                case 'added':
                    result.append(f"{indent_4}  + {key}: {value['value']}")
                case 'deleted':
                    result.append(f"{indent_4}  - {key}: {value['value']}")
                case 'nasted':
                    result.append(f"{indent_4}{key}: {stylish(value['value'])}")
                case 'changed':
                    old_value = value.get('old_value', 'No old value')
                    new_value = value.get('new_value', 'No new value')
                    result.append(f"{indent_4}  - {key}: {value['old_value']}")
                    result.append(f"{indent_4}  + {key}: {value['new_value']}")
                case 'unchanged':
                    result.append(f"{indent_4}  {key}: {value['value']} ")
    return '\n'.join(result)
