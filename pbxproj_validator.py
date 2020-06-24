#!/usr/bin/python
import sys

# Stack to keep track of parenthesis
validator_stack = []
# Stack to keep track of each parenthesis line number
validator_stack_line = []
# Lists of valid open parenthesis
open_list = ["{","("] 
# List of valid closed parenthesis
close_list = ["}",")"]
# Variable to keep track of line count
line_count = 0

"""
Main method
"""
def main(argv):
    if len(sys.argv) < 2:
        print("Please provide file path")
        sys.exit(1)

    pbxproj_path = str(sys.argv[1])
    print(pbxproj_path)
    verify(pbxproj_path)

"""
Method to verify pxproj file
Parameters: Path of pxproj file
"""
def verify(filepath):
    fh = open(filepath, "r")
    while True:
        global line_count
        line_count += 1
        line = fh.readline()
        if not line:
            break
        parse(line)
    fh.close()
    if len(validator_stack) == 0: 
        print("Validation Completed!!!")
        sys.exit(0)
    else: 
        print("Validation completed with error")
        sys.exit(1)

"""
Method to balance parenthesis
Parameter: Pbxproj line
"""
def parse(line):
    for char in line: 
        if char in open_list: 
            global line_count
            validator_stack.append(char) 
            validator_stack_line.append(line_count)
        elif char in close_list: 
            if ((len(validator_stack) > 0) and
                (char == validator_stack[len(validator_stack)-1])): 
                validator_stack.pop()
                validator_stack_line.pop()
            else:
                print("Detected error at line: " + str(validator_stack_line[len(validator_stack) - 1]))
                sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])