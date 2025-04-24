import pytest
from gendiff.scripts.gen_diff import main

@pytest.mark.parametrize("file1, file2, format, result", [
							("tests/fixtures/file1.json",
							"tests/fixtures/file2.json",
							"json",
							"tests/fixtures/result_json"),
							('tests/fixtures/file1.yml',
							'tests/fixtures/file2.yml',
							'yml',
							'tests/fixtures/result_yml'),
							('tests/fixtures/file1_nested.json',
							'tests/fixtures/file2_nested.json',
							'json',
							'tests/fixtures/result_stylish')])
def test_generate_diff(file1, file2, format, result):
	with open(result) as file:
		expected = file.read()
	assert generate_diff(file1, file2, format) == expected

