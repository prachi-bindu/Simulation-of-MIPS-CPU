# importing regex library for splitting the given file input with multiple delimiters
import re

# initializing four files
file1 = 'inst.txt'
file2 = 'config.txt'
file3 = 'data.txt'
file4 = 'reg.txt'

# list that stores instruction line by line
list1 = []
list2 = []
array2 = []
line_arr_file3 = []
line_arr_file4 = []
list4 = []
l4 = []

def file_parser():
    # Reading instructions from inst.txt line by line
    with open(file1) as fp:
        print('reading file1')
        line_arr_file1 = fp.readline()
        while line_arr_file1:
            inst1 = line_arr_file1.strip()
            # print(line_arr_file1.strip())
            line_arr_file1 = fp.readline()
            # array1 = inst1.split(", ")
            array1 = re.split(': | |, |    ',inst1)
            # print(array1)
            list1.append(array1)
        # print(list1)

    # Reading config.txt
    with open(file2) as fp:
        print('reading file2')
        line_arr_file2 = fp.readline()
        while line_arr_file2:
            inst2 = line_arr_file2.strip()
            # print(line_arr_file2.strip())
            line_arr_file2 = fp.readline()
            array2 = re.split(': |, ', inst2)
            list2.append(array2)
            # print(array2)

    # reading data.txt
    with open(file3) as fp:
        print('reading file3')
        line_arr_file3 = fp.readline()
        while line_arr_file3:
            inst3 = line_arr_file3.strip()
            # print(line_arr_file3.strip())
            line_arr_file3 = fp.readline()

    # Reading reg.txt
    with open(file4) as fp:
        print('reading file4')
        line_arr_file4 = fp.readline()
        while line_arr_file4:
            inst4 = line_arr_file4.strip()
            # print(line_arr_file4.strip())
            line_arr_file4 = fp.readline()
            list4 = list(line_arr_file4.strip())
            l4.append(list4)
            print(list4)
# Defining an integer variable that keeps the count of number of cycles
cycle = 0
file_parser()
# Defining a function that performs Instruction Fetch
# def instruction_fetch():
#     print("Hello from IF")
#     file_parser()
#     print(list1)
#     for instruction in list1:
#         # print(instruction)
#         instruction_decode(instruction)
#
# def instruction_decode(instruction):
#     print(instruction)
# instruction_fetch()