with open('data.db') as f:
    random_ints = f.readlines()

def mergesort(random_ints):
    middle = len(random_ints)/2
    first_half = random_ints[0:middle]
    second_half = random_ints[(middle+1):len(random_ints)]
