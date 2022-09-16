# Selection sort is an algorithm that sort a list based on the 
# minimum value found while iterating a list/array
def selection_sort(list):
    if(len(list) <= 1):
        return list
    sorted_list = []
    min_value = 0
    index_to_exclude = 0
    original_len = len(list)
    while len(sorted_list) != original_len:
        for i in range(len(list) - 1):
            if(list[i] <= list[min_value]):
                index_to_exclude = i
        sorted_list.append(list[index_to_exclude])
        list.pop(index_to_exclude)        
    return sorted_list