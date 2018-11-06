# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:34:52 2018

@author: Gautam Biswas
"""

"""
Peak finder

Start at the middle.  Look left, look right.  Choose 
larger, go in that direction.  Look at the next element to the current
element.  If next element is larger keep going.  If not we have found
a peak

"""
import random

number_of_elements = 3
peaklist = random.sample(range(1, 100), number_of_elements)
print (peaklist)
current_index = int(number_of_elements/2)

# assume list is at least 3 elements
 
peakvalue = False
while not peakvalue:
# if first or last element of list we are done.  We
# are assuming list sizes of at least 3
    if current_index in (0,number_of_elements - 1):
        peakvalue = True
        print (peaklist[current_index])
    elif (peaklist [current_index + 1] > peaklist [current_index]):
        current_index = current_index + 1
    elif (peaklist [current_index - 1] > peaklist [current_index]):
        current_index = current_index - 1  
    else:
        peakvalue = True
        print (peaklist[current_index])
        
    
    

    
