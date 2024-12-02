from gendiff.data import get_data


def generate_diff(file1, file2, format_name='stylish'):
    file1 = get_data(file1)
    file2 = get_data(file2)
    keys = sorted(set(file1.keys() | file2.keys()))
    result = []
    for key in keys:
        if not file2.get(key):
            result.append(f"- {key} : {file1.get(key)}")
        elif file1.get(key) == file2.get(key):
            result.append(f" {key} : {file1.get(key)}")
        elif not file1.get(key):
            result.append(f"+ {key} : {file2.get(key)}")
        else:
            result.append(f"- {key} : {file1.get(key)}\n+ {key} : {file2.get(key)}")
    return '\n'.join(result)

#модуль в котором прописываем добавление type. В нем же формируем построениие дерева - т.е. условия присваивания type
#пишем форматтер stylish
#добавляем в generate_diff formatter