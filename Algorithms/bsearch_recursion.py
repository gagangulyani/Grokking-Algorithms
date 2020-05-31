"""
    Binary Search using Recursion
"""
from random import randint


def bsearch(arr, ele, beg, end):
    if beg > end:
        return -1

    mid = (beg + end) // 2
    
    if arr[mid] == ele:
        return mid

    elif arr[mid] < ele:
        beg = mid + 1

    else:
        end = mid - 1
        
    return bsearch(arr, ele, beg, end)


if __name__ == '__main__':
    while True:
        # generating list of random integers
        l = [randint(-10000, 10000) for i in range(randint(1, 100000))]
        
        # removing duplicates
        l = list(set(l))
        
        # sorting the list
        l.sort()
        
        # last index of list
        n = len(l) -1 

        print("Size of List", n+1)

        # element to be searched
        ele = l[randint(0, n)]
        print(ele)
        
        result1 = l.index(ele)
        result2 = bsearch(l, ele, 0, n)
        
        print(result1, result2)
        if result1 == result2:
            print("Ok!")
        else:
            print("Error!")
            break
