# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:08:23 2018

@author: Gautam
"""

"""
Quicksort

Test cases:

sort_this_list = []
sort_this_list = [8,4]
sort_this_list = [8,4,10]
sort_this_list = [-5]*6
sort_this_list = [-45,-76,-21,0,8,-3] (even number of elements)
sort_this_list = [-45,-76,-21,0,8,-3, 19] (odd number of elements)
sort_this_list = [-5,-4,-3,-2,0,1,3,5] (already sorted)

Written recursively one of the key understandings in this algorithm
was that the list is not sorted at each iteration.  The
list is merely ordered around the pivot.  The assumption behind this algorithm
is that if the left half is sorted and the right half is sorted around the pivot
then the entire list is sorted.  However, how do we know when a list is sorted?  All
we are doing at each step is dividing the list around the pivot into greater than and
less than.

For example
after the first iteration,

[-45,-76,-21,0,8,-3]

will resemble [-45,-76,-21,-3,0,8]
The elements around the pivot, 0, are divided into greater than
on the right and less than on the left.  However, these two 
groups are not ordered, -76 < -45.  
How do we detect the end of recursion? As the recursions
progress there has to be a point when ordered = sorted.  Ordred 
and sorted become the same thing.  One way to detect this state is
to see if the list changed between recursions.  When the list has
stopped changing we are done.  However in code this is difficult to do.
If we merely look at the length of the lists being sorted we can not tell whether
we are done. 

Example:
    
    [2,1,3]

1 is the midpoint.  The list has one element on each side but is not sorted.
Would a test for number of elements in the halves of the list suffice as an 
end of recursion test? No, because we are not done.  The sorted list 
is [1,2,3] which also has one element in each half.  How do we differentiate
between these two configurations?

The choice I made was to force a sort when the number of elements was less than
or equal to 3.  For a 4 element list we can continue with the algorithm, but once
the list length is 3 or less I force a sort.

By contrast the merge sort steps when either half list is consumed

"""

# Choose the middle element for the pivot
# Order the right half first, then the left

def quicksort(sort_this_list):
    if len(sort_this_list) <= 3:
        sort_this_list.sort()
        return sort_this_list
    pivot = int(len(sort_this_list)/2)
    pivot_element = sort_this_list[pivot]
    right_half = sort_this_list[pivot + 1:]
    left_half = sort_this_list[:pivot]
    right_half_len = len(right_half)
    left_half_len = len(left_half)
    listindex = 0
    for no_of_elements in range(right_half_len):
        if right_half[listindex] < pivot_element:
            left_half.append(right_half.pop(listindex))
        else:
          # advance the listindex
          listindex += 1
    listindex = 0       
    for index in range(left_half_len):
        if left_half[listindex] > pivot_element:
            right_half.append(left_half.pop(listindex))
        else:
            #advance listindex
            listindex += 1
    sorted_list = [pivot_element] + quicksort(right_half)
    sorted_list = quicksort(left_half) + sorted_list
    return sorted_list


sort_this_list = []
sort_this_list = [8,4]
sort_this_list = [8,4,10]
sort_this_list = [-5]*6
sort_this_list = [-45,-76,-21,0,8,-3, 19]
sort_this_list = [-5,-4,-3,-2,0,1,3,5]

print (quicksort(sort_this_list))


