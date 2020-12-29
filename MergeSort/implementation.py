# Time complexity = O(nlogn)
# Space Complexity = O(n)
def merge_sort(array):
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = array[0:middle]
    right = array[middle:len(array)]
    # print(left, right)

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    container = []
    left_index = 0
    right_index = 0
    while True:
        if left[left_index] <= right[right_index]:
            if left_index == len(left) - 1:
                container.append(left[left_index])
                container.extend(right[right_index:])
                break
            container.append(left[left_index])
            left_index += 1
        else:
            if right_index == len(right) - 1:
                container.append(right[right_index])
                container.extend(left[left_index:])
                break
            container.append(right[right_index])
            right_index += 1
    return container
