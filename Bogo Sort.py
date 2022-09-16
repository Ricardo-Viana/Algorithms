#Bogo sort is an algorithm that randomly sort a list/array
from asyncio.windows_events import NULL
import random


def bogo_sort(list):
    if(list <= 1):
        return list
    while sort_of_bogo_sort(list) != True:
        random.shuffle(list)
    return list
def sort_of_bogo_sort(list):
    value = NULL
    for i in range(len(list) - 1 ):
        if(list[i] > list [i + 1]):
            value = False
            break
        else:
            value = True
    return value