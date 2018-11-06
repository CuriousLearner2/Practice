# -*- coding: utf-8 -*-
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""
"""

Initialize two pointers, one for the current element, the other 
for the neighbor.

Loop till neighbor equals length of list 

Remove duplicates as list is traversed.

"""

inputlist = [1,1,1,2,3,3,4,5,5,5,6]
current = 0
neighbor = 1

input_length = len(inputlist)


while (neighbor < input_length):
    more_duplicates = True
    while(neighbor < input_length and more_duplicates):
        if (inputlist[neighbor] == inputlist[current]):
            inputlist.pop(neighbor)
            input_length -= 1
        else:
            more_duplicates = False
        
    current = neighbor
    neighbor += 1

print (input_length)

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9, Because nums[ 0 ] + nums[ 1 ] = 2 + 7 = 9, return [ 0 , 1 ].
"""

"""
For each element subtract element from target.
Look for this number in the list.  If found we are done

If not found, pop the element, subtract 0th element
from target and look again.

"""

inputlist = [1,4,6,8,10]
target = 18
found = False
addend1_index = 0
inputlist_len = len(inputlist)
while (inputlist) and not found:
    addend2 = target - inputlist[0] 
    try:
        addend2_index = inputlist.index(addend2)
    except:
        addend2_index = None
        inputlist.pop(0)
        addend1_index += 1
    if (addend2_index):
        indices = [addend1_index,addend1_index + addend2_index]
        found = True
print (indices)
      

"""
alternate solution posted in the cafe

def twoSum(nums, target):
    for index, item in enumerate(nums):
        try:
            return index, nums.index(target - item, index + 1) 
        except ValueError:
            Pass
Traverses the entire list though to get the second addend
but aborts comprehension when answer is found


"""

"""

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""



"""

Take a head node, find tail of head node
Point tail to head
Tail now becomes head
At end of list?
If not, find tail.

Apparently no linked list data structure exist
in Python.  There is a double ended queue dequeue in 
collections module.

Will use regular list instead.

node a sub n should be swapped with node a sub (length of list - 1 - n)

"""

inputlist = [1,4,6,8,10,12]
input_len = len(inputlist)
for index in range(int(input_len/2)):
    temp = inputlist[index]
    inputlist[index] = inputlist[input_len - 1 - index]
    inputlist[input_len - 1 - index] = temp

    
