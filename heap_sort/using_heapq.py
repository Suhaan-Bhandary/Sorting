import heapq
# does not change the input.
def heap_sort(taken_array):
    array = taken_array.copy()
    min_list = []
    heapq.heapify(array)  # O(n log n)
    for _ in range(len(array)):  # O(n)
        min_list.append(heapq.heappop(array))  # O(log n) + O(1)
    return min_list


array_one = [1, 2, 8, 4, 5, 9, 10, 25, 48, 3]
print(heap_sort(array_one))
print(array_one)
# Heapsort is not stable because operations on the heap can change the relative order of equal items.
