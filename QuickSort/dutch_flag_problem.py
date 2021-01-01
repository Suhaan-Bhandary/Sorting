# Given an array A[] consisting 0s, 1s and 2s.
# The task is to write a function that sorts the given array. The
# functions should put all 0s first, then all 1s and all 2s in last.

def dutch_sort(array):
    low = 0
    high = len(array) - 1  # Upper bond,,if confuse read the description down in hoare_to_handle_duplicate
    mid = 0
    # Mid will traverse all over the array, So :
    while mid <= high:
        print(array)
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        elif array[mid] == 2:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
            # Here we are not increasing the value of mid as we don't Know the value.
        else:
            mid += 1

    return array


if __name__ == '__main__':
    print(dutch_sort([1, 2, 0, 0, 1, 2, 1, 1, 0]))
