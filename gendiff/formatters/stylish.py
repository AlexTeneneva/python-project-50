

def stylish(diff: dict):
    types = diff.get('type')
    keys = sorted(diff.keys())
    result = {}
    indent_4 = '    '
    for key, value in diff.items():
        match types:
            case 'added':
                result.append(f"{indent_4}  + {key}: {value['value']}")
            case 'deleted':
                result.append(f"{indent_4}  - {key}: {value['value']}")
            case 'nasted':
                result.append(f"{indent_4}{key}: stylish(value['value'])")
            case 'changed':
                result.append(f"{indent_4}  - {key}: {value['old_value']}")
                result.append(f"{indent_4}  + {key}: {value['new_value']}")
            case 'unchanged':
                result.append(f"{indent_4}*2{key}: {value['value']} ")
    return '/n'.join(result)
