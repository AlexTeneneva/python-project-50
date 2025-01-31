#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
from gendiff.gendiff import generate_diff as gendiff
from gendiff.cli import invitation


def main():
    first_file, second_file, format = invitation()
    print(gendiff(first_file, second_file, format))


if __name__ == '__main__':
    main()
