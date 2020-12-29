def selection_sort(arr):
    for counter in range(len(arr)):
        small_index = counter
        for j in range(counter+1, len(arr)):
            if arr[small_index] > arr[j]:
                small_index = j
        arr[small_index], arr[counter] = arr[counter], arr[small_index]
# Big O of Bubble sort:
# Time Complexity = O((n**2/2)+(n/2))
#                 = O(n**2)
# Space Complexity = O(1)


array = [2, 5, 1, 8]
selection_sort(array)
print(array)
