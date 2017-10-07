import sys
import os

class ArgumentsErrors(ValueError):
    pass

def get_input_files(arguments):
    if len(arguments) == 3:
        return arguments[1], arguments[2]
    else:
        raise ArgumentsErrors("Invalid Argurments.")


def read_file(filename):
    with open (filename, "r") as fd :
        line = fd.readline()
#        for line in fd:
        return line;

def parse_text(text):
    text = text.replace("\n", "")
    text = text.replace(".", "")
    words = text.split(" ")

    return words

def diff(cont1, cont2):
    if(cont1 == cont2):
        return "I'm batman www!", "I'm batman www!"

if __name__ == '__main__':
    file1, file2 = get_input_files(sys.argv)

