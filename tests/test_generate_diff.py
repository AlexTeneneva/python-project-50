import pytest
from gendiff.gendiff import generate_diff

@pytest.mark.parametrize("file1, file2, format, result" [
							 ('tests/fixtures/file1.json'
							  'tests/fixtures/file2.json'
							  'json'
							  'tests/fixtures/result')
						 ])
def test_generate_diff(file1, file2, format, result):
	assert generate_diff(file1, file2, format) == result