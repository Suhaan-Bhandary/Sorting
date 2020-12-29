from math import log2, ceil

# First Step towards Heap Sorting.
def heap_sort(li):  # BigO(NlogN)
    sorted_array = []
    heaped_list = heapify(li)

    while len(heaped_list) > 1:  # As the first element is the root or the start[Not a part of binary tree] O(n)
        sorted_array.append(heaped_list[1])
        last_element = heaped_list[-1]
        del heaped_list[-1]
        if len(heaped_list) == 1:
            break
        heaped_list[1] = last_element
        if not valid_min_heap(heaped_list):
            heaped_list = heapify(heaped_list)  # O(logN)
    del heaped_list[0]
    return sorted_array

def valid_min_heap(li):
    number_of_node = len(li) - 1
    for i in range(1, number_of_node):
        if 2 * i <= number_of_node or (2 * i) + 1 <= number_of_node:  # Checking if any children are their.
            if (2 * i) + 1 <= number_of_node:  # Both children are present.
                if li[i] <= li[2 * i] and li[i] <= li[2 * i + 1]:  # Is the Node satisfying heap condition.
                    continue
                else:
                    return False
            elif 2 * i <= number_of_node:  # left children is present.
                if li[i] <= li[2 * i]:  # Is the Node satisfying heap condition.
                    continue
                else:
                    return False
        else:
            break
            # if we reached till the i where no children are there for the node then it means that the above
            # code ran and no mistake was found.
    return True  # if no above returns are ran. # we can use to check

def heapify(li):
    length = len(li) - 1
    height = ceil(log2(length + 1)) - 1  # second last level height.
    i = 2 ** height - 1  # second last level last element index element index,as we take "*" at index 0
    # print(i, "***", li, length, height)
    # We are taking look at second last line if it is not full.
    # One can notice it if you see floor or 46 line.
    # input()
    while i > 0:
        min_child_index = min_child(i, li, length)
        if min_child_index is not False:
            li[i], li[min_child_index] = li[min_child_index], li[i]
        i -= 1
        # print(i)
    # input()
    return li

def min_child(index, iterable, iter_len):
    if (index * 2) > iter_len:
        return False
    elif (index * 2) == iter_len:
        if iterable[index * 2] < iterable[index]:
            return index * 2
        return False
    else:
        if iterable[index * 2] < iterable[(index * 2) + 1]:
            if iterable[index * 2] < iterable[index]:
                return index * 2
            else:
                return False
        else:
            if iterable[(index * 2) + 1] < iterable[index]:
                return (index * 2) + 1
            else:
                return False


heap = ["*", 9, 1, 7, 2, 5, 6, 3]

print(heap_sort(heap))
