import sys

class ArgumentsErrors(ValueError):
    pass

def get_input_files(arguments):
    if len(arguments) == 3:
        return arguments[1], arguments[2]
    else:
        raise ArgumentsErrors("Invalid Argurments.")


def read_file(filename):
    pass
        


if __name__ == '__main__':
    file1, file2 = get_input_files(sys.argv)

