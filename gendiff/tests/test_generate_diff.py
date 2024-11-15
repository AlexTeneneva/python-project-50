from gendiff.gendiff import generate_diff

file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}

file2 = {
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}

result = {
	'host: hexlet.io'
	'- follow': false,
	'- proxy: 123.234.53.22'
	'- timeout': 50,
	'+ timeout': 20,
	'+ verbose': true
	}

format = '.json'

def test_generate_diff():
	assert generate_diff(file1, file2, format) == result