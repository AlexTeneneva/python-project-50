def make_depth(depth):
    return f" {depth * 4}"

def make_symbol(symbol=" "):
    return f" {symbol} "

def stylish(diff, depth=0):
    indent = make_depth(depth)
    result = []
    children = diff.get('children')
    for item in children:
        name = item.get('name')
        type = item.get('type')
        value = item.get('value')
        to_format = to_format(value, depth+1)
        old = to_format(item.get("old_value"), depth+1)
        new = to_format(item.get("new_value"), depth+1)
        if type == 'added':
            result.append(f"{indent}{make_symbol("+")} {name}: {to_format}")
        if type == "deleted":
            result.append(f"{indent}{make_symbol("-")} {name}: {to_format}")
        if type == "nested":
            _symbol = make_symbol()
            result.append(f"{indent}{_symbol} {name}: {stylish(item, depth+1)}")
        if type == "changed":
            result.append(f"{indent}{make_symbol("-")} {name}: {old}")
            result.append(f"{indent}{make_symbol("+")} {name}: {new}")
        if type == 'unchanged':
            result.append(f"{indent}{make_symbol()} {name}: {to_format}")
    tree = "\n".join(result)
    return f"{{\n{tree}\n{indent}}}"

def to_format (value, depth):
    indent = make_depth(depth)
    result = []
    if value is None:
        return 'null'
    if isinstance (value, int):
        return value
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        for key, row in value.items():
            result.append(
                f"{indent}{make_symbol()}{key}: {to_format(row, depth + 1)}"
            )
        format = '\n'.join(result)
        return f"{{\n{format}{indent}}}"
    return f"{value}"