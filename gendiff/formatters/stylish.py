indent_4 = '    '


def stylish(diff: dict):






#достаю все types,
# задаю условие для каждого type с отступами и построением строки через match (учимся использовать)
#протестировать '\n'.join в форматтере и в гендифф
#добавить условие если value is none -> return 'null'
# в nested нужно вызвать функцию рекурсивно

#    for key in keys:
        if not file2.get(key):
            result.append(f"- {key} : {file1.get(key)}")
        elif file1.get(key) == file2.get(key):
            result.append(f" {key} : {file1.get(key)}")
        elif not file1.get(key):
            result.append(f"+ {key} : {file2.get(key)}")
        else:
            result.append(f"- {key} : {file1.get(key)}\n+ {key} : {file2.get(key)}")


