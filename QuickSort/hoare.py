from math import floor


def quick_sort(array, low, high):
    if low < high:
        point = partition(array, low, high)
        quick_sort(array, low, point)
        quick_sort(array, point + 1, high)


def partition(array, low, high):
    pivot = array[floor((low+high)/2)]
    # In the above by using floor we are avoiding the case where pivot = array[high]
    #  If not done it will cause infinite recursion.
    # For the code in the question, the pivot can be any element except a[hi].
    # Example of the issue with pivot = a[hi], consider the case where lo = 0, hi = 1, and a[0] < a[1].

    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    arr = [1, 7, 2, 6, 5, 9, 8, 10]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
