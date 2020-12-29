def bubble_sort(arr):
    for a in range(len(arr)):
        for i in range(len(arr) - 1 - a):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Big O of Bubble sort:
# Time Complexity = O((n**2/2)+(n/2))
#                 = O(n**2)
# Space Complexity = O(1)
if __name__ == '__main__':
    array = [7, 4, 5, 2]
    bubble_sort(array)
    print(f"Bubble Sort : {array}")
