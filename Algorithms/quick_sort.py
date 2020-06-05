"""
    Quick Sort
        It uses first element in List as Pivot element
        (from Grocking Algorithms)
"""
from random import randint


def quick_sort(arr):
    if len(arr) < 2:
        # No need to sort an List with 1 element
        return arr

    pivot = arr[0]

    less = [i for i in arr[1:] if i <= pivot]
    more = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(more)


if __name__ == '__main__':
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
