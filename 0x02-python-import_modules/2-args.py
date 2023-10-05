#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    num_arguments = len(arg) - 1
    if num_arguments > 1:
        print("{:d} arguments.".format(num_arguments))
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, arg[i]))
    elif num_arguments == 0:
        print("{} arguments.".format(num_arguments))
    else:
        print("{} argument:".format(num_arguments))
        print("{}: {}".format(num_arguments, arg[i]))
