# Mergesort algorithm

def merge(list1, list2):
    temp_list = []
    j = 0
    for x in range(0, len(list1)):
        while(j < len(list2) and list2[j] < list1[x]):
            temp_list.append(list2[j])
            j = j+1

        temp_list.append(list1[x])

    while(j <= len(list2)-1):
        temp_list.append(list2[j])
        j+=1
    print temp_list 
    return temp_list


def mergesort(int_list, first, end):

    if first != end:
	middle = (first + end) / 2
       
        first_half = mergesort(int_list, first, middle)
        second_half = mergesort(int_list, middle+1, end)
        return merge(first_half, second_half)
    else:
        temp_list = []
        temp_val = int_list[first] 
        temp_list.append(temp_val)
        return temp_list

with open('data.db') as f:
    random_ints = f.read().split('\n')

print random_ints

mergesort(random_ints, 0, len(random_ints)-1) 
