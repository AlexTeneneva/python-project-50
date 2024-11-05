import argparse

def invitation():
    parser = argparse.ArgumentParser(
                    description='Compares two configuration files and shows a difference.',
                   )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-h', '--help', help='show this help message and exit')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.help
