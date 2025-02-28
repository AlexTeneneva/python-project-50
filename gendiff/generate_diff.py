from gendiff.data import get_data
from gendiff.formatters.stylish import stylish
from gendiff.diff_builder import create_diff


def generate_diff(file1, file2, format_name='stylish'):
    file1 = get_data(file1)
    file2 = get_data(file2)
    diff = create_diff(file1, file2)
    return stylish(diff)
