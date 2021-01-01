from math import floor


def quick_sort(array, low, high):
    if low < high:
        left, right = partition(array, low, high)
        quick_sort(array, low, left - 1)
        quick_sort(array, right, high)


def partition(array, low, high):
    pivot = array[floor((low + high) / 2)]

    left = low
    right = low
    upper_bound = high  # Upper bond help me to locate the swaps in line 22(elif array[right] > pivot).
    while right <= upper_bound:
        if array[right] < pivot:
            array[right], array[left] = array[left], array[right]
            left += 1
            right += 1
        elif array[right] > pivot:
            array[right], array[upper_bound] = array[upper_bound], array[right]
            upper_bound -= 1
            # Notice here we are only changing the upper limit
        else:
            # the element is equal to pivot
            right += 1
    print(array)
    print(left, right)
    return left, right


if __name__ == '__main__':
    arr = [1, 5, 7, 2, 6, 5, 5, 9, 5, 8, 10]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

# It uses three indices left, current(right) and upper_bond (left, right, and upper bound),
# maintaining the following invariant in the while loop.
# --------------------------------------------------------------------
# low ≤ left ≤ right ≤ upper_bond ≤ high
# the elements with index in [low, left) are smaller to the pivot.
# the elements with index in [left, right) are equal to the pivot.
# the elements with index in [right, upper_bound] are not examined yet.
# the elements with index in (upper_bond, high] are greater than the pivot.
# There are a few minor variants. The above should be enough for you to understand what is going on.
