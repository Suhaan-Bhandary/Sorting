from math import floor


def quick_sort(array, low, high):
    if low < high:
        point = partition(array, low, high)
        quick_sort(array, low, point - 1)
        quick_sort(array, point + 1, high)


def partition(array, low, high):
    mid = floor((low + high) / 2)
    if array[mid] < array[low]:
        array[mid], array[low] = array[low], array[mid]
    if array[high] < array[low]:
        array[high], array[low] = array[low], array[high]
    if array[mid] < array[high]:
        array[mid], array[high] = array[high], array[mid]

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
