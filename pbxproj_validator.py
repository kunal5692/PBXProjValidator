#!/usr/bin/python
import sys

stack = []
open_list = ["{","("] 
close_list = ["}",")"]

def main(argv):
    if len(sys.argv) < 2:
        print("Please provide file path")
        sys.exit(1)

    pbxproj_path = str(sys.argv[1])
    print(pbxproj_path)
    verify(pbxproj_path)

def verify(filepath):
    fh = open(filepath, "r")
    while True:
        line = fh.readline()
        parse(line)


def parse(myStr):
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"

if __name__ == "__main__":
    main(sys.argv[1:])