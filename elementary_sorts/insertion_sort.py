# It is very useful when we know that the list is pretty much sorted.
def insertion_sort(arr):
    for counter in range(1, len(arr)):
        current_position = counter
        if arr[current_position] > arr[current_position - 1]:
            continue
        else:
            while current_position > 0:
                if arr[current_position] < arr[current_position - 1]:
                    arr[current_position], arr[current_position - 1] = arr[current_position - 1], arr[current_position]
                current_position -= 1


# Big O of Bubble sort:
# Time Complexity = O(n**2)
# Space Complexity = O(1)

array = [2, 5, 1, 8]
insertion_sort(array)
print(array)
