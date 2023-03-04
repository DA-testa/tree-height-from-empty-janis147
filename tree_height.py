# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    heights = np.zeros(int(n))
    max_height = 0

    for i in range(int(n)):
        if heights[i] > 0:
            continue

        height = 0
        j = i
        while j != -1:
            if heights[j] > 0:
                height += heights[j]
                break
            else:
                height += 1
                j = int(parents[j])

        heights[i] = height
        if height > max_height:
            max_height = height

    return max_height

def input_from_keyboard():
    try:
        n = input()
        parents = input()
        print(str(n))
        parents = parents.split(" ")
        return n, parents
    except:
        n = 0
        parents = 0
        return n, parents

def main():
    input_method = input()
    n, parents = input_from_keyboard()
    if n and parents:
        height = compute_height(n, parents)
        print(int(height))
    else:
        print("ERROR2")


sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()