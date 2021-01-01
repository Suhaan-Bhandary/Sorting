# Lomuto's Quick sort.

# It takes last element in the sub array as the pivot.

# As this scheme is more compact and easy to understand, it is frequently used in introductory material,
# although it is less efficient than Hoare's original scheme
# e.g.,when all elements are equal.This scheme degrades to O(n**2) when
# the array is already in order.

def quick_sort(array, low, high):
    if low < high:
        point = partition(array, low, high)
        quick_sort(array, low, point - 1)
        quick_sort(array, point + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


if __name__ == '__main__':
    arr = [1, 7, 2, 6, 5, 9, 8, 10]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
