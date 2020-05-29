"""
    This Program counts total number of items in a List using recursion
"""
from random import randint


def count_rec(arr):
    """
        This function takes List (arr) and Index Number
        then finds the number of elements in it using Recursion.
    """
    if not arr:
        return 0
    return 1 + count_rec(arr[:-1])


if __name__ == "__main__":

    while True:
        # Stress Testing
        arr = [randint(-1000, 1000) for i in range(0, randint(2, 990))]

        result1 = count_rec(arr)
        result2 = len(arr)

        print(result1, result2)

        if result1 == result2:
            print("Okay!")
        else:
            print("Error!")
            break
