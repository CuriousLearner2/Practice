listA = [0,1,3,4,5,6,9,12]
listA = [-1,2,4,6,7,15,43,49]
listA = []

import math


def merge_sort (sort_this_list):
    sort_len = len(sort_this_list)
    merged_list = []
    while sort_len > 0:
        number_of_sorts = int(math.log(sort_len,2))
        sort_len = 2 ** number_of_sorts
        sliced_sort = sort_this_list[:sort_len]
        sort_this_list = sort_this_list[sort_len:]
        merged_list += sort_powers_of_two_lists(sliced_sort)
        if len(merged_list) > 1:
            merged_list = merge_sort_two(merged_list[0],merged_list[1])
        sort_len = len(sort_this_list)
    return merged_list

    


def merge_sort_two(listA,listB):
# 1 list with two sublists to be merged
    merged = []
    listA_len = len(listA)
    listB_len = len(listB)
    while listA_len > 0 and listB_len > 0:
            if listA[0] < listB[0]:
                merged.append(listA.pop(0))
            elif listB[0] < listA[0]:
                merged.append(listB.pop(0))
            else:
                merged.append(listA.pop(0))
                merged.append (listB.pop(0))
            listA_len = len(listA)
            listB_len = len(listB)
    if listA_len == 0:
        merged += listB
    elif listB_len == 0:
        merged += listA
    return merged


def sort_powers_of_two_lists(sort_this_list):
# make one element lists out of the list members
    sort_this_list = [[element] for element in sort_this_list]
    merged_list = []
    while len(sort_this_list) > 1:
        first = sort_this_list.pop(0)
        second = sort_this_list.pop(0)
        merged_elements = merge_sort_two(first,second)
        merged_list += [merged_elements]
        if len(sort_this_list) == 0:
            sort_this_list = merged_list
            merged_list = []
            
    return sort_this_list




   
"""
power_of_two = Take log base 2 of list

slice list to 2 ** power_of_two 

Take sorted_list till now.  Add in sliced list as a list,
not as elements

Give it to merge_sort_two to merge sort.

keep going until no more list left.


"""

listA = [-1,2,7,6,4,43,15,49,6,2,10,-8]

listA = [-1,2,7,6,4,43,15,49,6,2]

listA = [-1,2,7,6,4,43,15,49]
print (sort_powers_of_two_lists (listA))

listA = [-1,2,7,6,4,43,15,49,6,2]
listA = [12,12]
print (merge_sort (listA))

