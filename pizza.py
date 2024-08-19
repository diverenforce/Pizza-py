import sys

def main():
    ...

def arg_length():
    return len(sys.argv) == 2

def arg_end():
    return sys.argv[1].endswith('.csv')




