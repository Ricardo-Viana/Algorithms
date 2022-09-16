# Quick sort is an algorithm that sort a list/array by picking a 
# target value creating sublists based on this target value, 
# separating numbers that are greater and less than the value
def quick_sort(list):
    if(len(list) <= 1):
        return list
    less_target = []
    greater_target = []
    target = list[0]
    for i in range(1,len(list)):
        if(list[i] > target):
            greater_target.append(list[i])
        else:
            less_target.append(list[i])
    return quick_sort(less_target) + [target] + quick_sort(greater_target)