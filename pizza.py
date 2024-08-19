import sys

def main():
    if arg_length() and len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif arg_length() and len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    
    if arg_end() == False:
        sys.exit('Not a CSV file')

    if arg_exist() != True:
        sys.exit('File does not exit')

def arg_length():
    return len(sys.argv) != 2

def arg_end():
    return sys.argv[1].endswith('.csv')

def arg_exist():
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        return False
    else:
        return True
    


if __name__ == '__main__':
    main()