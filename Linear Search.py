#Linear search is an algorithm of searching, 
# that searches a key iterating all the list/array 
def linear_search(list,key):
    if(len(list) == 1):
        return 0
    for i in range(1, len(list)):
        if list[i] == key:
            return i
    return -1