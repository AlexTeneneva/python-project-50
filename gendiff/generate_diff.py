from gendiff.data import get_data
from gendiff.formatters.stylish import stylish
from gendiff.diff_builder import build_root


def generate_diff(file1, file2, format_name='stylish'):
    file1 = get_data(file1)
    file2 = get_data(file2)
    diff = build_root(file1, file2)
    #return diff
    return stylish(diff)
