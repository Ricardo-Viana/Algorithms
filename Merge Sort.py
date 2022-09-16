def merge_sort(list):
    if(len(list) <= 1):
        return list
    middleIndex = len(list) // 2
    left_side = merge_sort(list[:middleIndex])
    right_side = merge_sort(list[middleIndex:])
    sorted_list = []
    index_right = 0
    index_left = 0
    while index_right < len(right_side) and index_left < len(left_side):
        if(right_side[index_right]) < (left_side[index_left]):
            sorted_list.append(right_side[index_right])
            index_right+= 1
        else:
            sorted_list.append(left_side[index_left])
            index_left+= 1
    sorted_list += left_side[index_left:]
    sorted_list += right_side[index_right:]
    return sorted_list
