# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 06:57:06 2018

@author: Gautam Biswas
"""

"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

https://codereview.stackexchange.com/questions/195449/firstduplicate-finder


"""
"""

Use the function I coded earlier to find duplicates using a binary search

"""



def find_dups(inputlist):
    inputlist_len = len(inputlist)
    minindices = {}
    for listindex in range(inputlist_len):
         element_tofind = inputlist.pop(0)
         try:
            getindex = inputlist.index(element_tofind) 
            minindices[listindex + getindex + 1 ] = element_tofind
         except:
             ValueError
             pass
    if minindices:
        result_index = min(minindices)
        result = minindices[result_index]
    else:
        result_index = None
        result = -1
    return (result_index,result)

find_dups([2, 1, 3, 5, 3, 2])
find_dups([2, 4, 3, 5, 1])

"""
Alternate solutions using list.count method which don't work
because count method counts multiple times for the same 
list element.

This list produces the following output 

inputlist = [2, 1, 3, 5, 3, 2]        
minindices = {listindex:value for listindex, value in enumerate(inputlist)
                if inputlist.count(value) > 1}
{0: 2, 2: 3, 4: 3, 5: 2}



"""

def find_dups2(inputlist):
    minindices = {}
    for listindex,value in enumerate (inputlist):
        if inputlist.count(value)  > 1 and value not in minindices.values() :
            minindices [listindex] = value
        if minindices:
            result_index = min(minindices)
            result = minindices[result_index]
        else:
            result_index = None
            result = -1
    return (result_index,result)

inputlist = [2, 1, 3, 5, 3, 2]
find_dups2(inputlist)

minindices = {}
inputlist = [2, 1, 3, 5, 3, 2]        
minindices = {listindex:value for listindex, value in enumerate(inputlist)
                if inputlist.count(value) > 1 and value not in minindices.values() }
print (minindices)

testdict =  {0: 2, 2: 3, 4: 3, 5: 2}

if 2 in testdict.values():
    print ('yes')
    
for key,value in testdict.items(testdict):
    if value ==2 :
        print (key)
    