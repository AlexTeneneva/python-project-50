#!/usr/bin/env python3

from gendiff.cli import invitation

def main():
    first_file, second_file, format = invitation()
    print(gendiff(first_file, second_file, format))


if __name__ == '__main__':
    main()
