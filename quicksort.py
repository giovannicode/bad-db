def partitiion(int_list, left, right:
    right = right+1
    while(left <= right)
	while(int_list[right] > pivot):
            left-=1

        while(int_list[left] < pivot):
            right+=1

        i
        
    return right

def quicksort(int_list, right, left):
    if begin != end:
        pivot = partition(int_list, right, left)
        quicksort(int_list, right, pivot-1)
        quicksort(int_list, pivot+1, left)




"""
def quicksort(int_list, right, left):
    if right != left:
	pivot = int_list[right]
        old_right = right
        old_left = left
 
     
        while(right != left): 
	    while(right!=left):
		if(int_list[left] < pivot):
		    temp = int_list[right]            
		    int_list[right] = int_list[left]
		    int_list[left] = temp
                    print "Switch " + str(temp) + " and " + str(int_list[right])
                    print int_list
                    break
		left-=1
      
            while(right!=left):
		if(int_list[right] > pivot):
		    temp = int_list[left]
		    int_list[left] = int_list[right]
		    int_list[right] = temp
                    print "Switch " + str(temp) + " and " + str(int_list[left])
                    print int_list
                    break
	        right+=1

        old_right = right
        old_left = left
	while(right != left):
	    if(i <= (len(int_list)-1) and int_list[i] < pivot):
		int_list[right] = int_list[i]
                right+=1
	    else:
		int_list[left] = int_list[i]
                left-=1
	    i+=1
        pivot = i"""
        print "anothe layer"
	quicksort(int_list, old_right, right-1)
        quicksort(int_list, right+1, old_left)


with open('data.db') as f:
    random_ints = map(int, f.read().split('\n'))

print random_ints 

quicksort(random_ints, 0, len(random_ints)-1)
