# Algorithm Binary Search, remembering the list has to be sorted
# Binary Search has two ways to be implemented, recursive and not recursive
# Binary search is an algorithm of searching that 
# search a key value spliting the list
def recursive_binary_search(list,key,first = 0, last = None):
    if last == None:
        last = len(list) - 1
    if first > last:
        return -1
    middleIndex = (first+last) // 2
    if(list[middleIndex] == key):
        return middleIndex
    elif(list[middleIndex] < key):
        return recursive_binary_search(list,key, middleIndex+1, last)
    elif(list[middleIndex] > key):
        return recursive_binary_search(list,key,first, middleIndex-1)

def binary_search(list,key):
    start = 0
    final = len(list) - 1
    while start <= final:
        middleIndex = (start+final) // 2
        if(list[middleIndex] == key):
            return middleIndex
        elif(list[middleIndex] > key):
            final = middleIndex - 1
        else:
            start = middleIndex + 1
    return -1