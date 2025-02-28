#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
from gendiff.generate_diff import generate_diff as gendiff
from gendiff.cli import invitation


def main():
    #first_file, second_file, format = invitation()
    #print(gendiff(first_file, second_file, format))
    print(gendiff('/home/alex/Git/python-project-50/tests/fixtures/file1.yml',
          '/home/alex/Git/python-project-50/tests/fixtures/file2.yml'))


if __name__ == '__main__':
    main()
