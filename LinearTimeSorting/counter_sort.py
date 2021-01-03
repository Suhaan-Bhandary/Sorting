def counter_sort_array(array,largest_element=100): # Assigned a default value if value is not passed in.
    tracker = [0]*(largest_element+1) # Making a list of k(largest_element) elements

    for x in array:
        tracker[x] += 1 # Traversing through the given array of positive integer and adding one to the value assciated with the key.
        # To keep track.

    output = []

    for i in range(largest_element+1): # Traversing through the tracker array and looking for non zero value of elements.
        for j in range(tracker[i]): # Check how many elemnets are their by value.
            output.append(i)
    return output

def counter_sort_dictionary(dictionary,largest_element):
    tracker = [0]*(largest_element+1) # Making a list of k(largest_element) elements

    for x in dictionary: # Remember that python will always give key when traversing.
        print(x)
        if tracker[x] == 0:
            tracker[x] = [dictionary[x]]
        else:
            tracker[x].append(dictionary[x])
    output = []

    for i in range(largest_element+1): # Traversing through the tracker array and looking for non zero value of elements.
        print(i,tracker[i])
        if tracker[i] != 0:
            output.extend(tracker[i])
    return output

if __name__ == '__main__':
    array_one = [0,10,10,10,10,10,10,12,5,8]

    # Rank example :
    dictionary_one = {
        1 : "suhaan",
        12 : "ram",
        8 : "sham",
        2 : "vivek",
        6 : "roll6",
        15 : "roll15",
        17 : "harsh"
    }

    print(counter_sort_dictionary(dictionary_one,10))
    print(counter_sort_array(array_one,17))
