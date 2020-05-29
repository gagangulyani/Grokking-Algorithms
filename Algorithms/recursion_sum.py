"""
    This Program calculates Sum of List using recursion
"""
from random import randint


def sum_rec(arr, i, n):
    """
        This function takes List (arr), Index Number and Length
        of List to sums the elements in it using Recursion.
    """

    if i == n:
        return 0
    return arr[i] + sum_rec(arr, i+1, n)


if __name__ == "__main__":

    while True:
        # Stress Testing
        arr = [randint(-1000, 1000) for i in range(0, randint(2, 990))]
        n = len(arr)

        result1 = sum_rec(arr, 0, n)
        result2 = sum(arr)

        print(result1, result2)

        if result1 == result2:
            print("Okay!")
        else:
            print("Error!")
            break
