"""
    Quick Sort
    (from Grokking Algorithms)
"""


def quick_sort(arr):
    if len(arr) < 2:
        # No need to sort a List with 0 or 1 element
        return arr

    # choosing first element in list as pivot element
    pivot = arr[0]

    # store elements from list less than or equal to
    # pivot element
    less = [i for i in arr[1:] if i <= pivot]

    # store elements from list greater than pivot element
    great = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(great)


if __name__ == '__main__':
    from random import randint

    while True:
        # Generate list of random integer ranging from size 1 to 100000
        # containing elements ranging from -10000 to 10000
        N = randint(1, 100000)

        arr = [randint(-10000, 10000) for i in range(1, N + 1)]

        print("\n\nSorting List of Size:", N)

        # Python's Built In Sorting function
        result1 = sorted(arr)
        print('List Sorted with Built-in Algo!')

        # Quick Sort
        result2 = quick_sort(arr)
        print('List Sorted with Quick!')

        if result1 == result2:
            print('Okay!')
        else:
            print('Error!!\n')
            print(result1)
            print(result2)
            break
