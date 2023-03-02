# python3

import sys
import threading
import numpy

def input_from_file(file_dir):
    with open(file_dir) as f:
        lines = f.readlines()
    
    print(lines)

    n = 10
    parents = 10
    return n, parents

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    while True:
        input_method = input("Input method [F or I]: ")
        if input_method == "F":
            file_dir = input("File directory: ")
            n, parents = input_from_file(file_dir)
            compute_height(n, parents)
        elif input_method == "I":
            break
        else:
            print("Try one more time!")

    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))