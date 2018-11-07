
"""
This code finds the number of occurrences of an element in a sorted list and
stores the indices in found_dict.  Finds only the first .  For example 

Input: 

sorted_list = [1,2,3,3,7,8,9,9]
number_to_find = 3

Output:
found_dict = {2: 3, 3: 3}

"""
# Divide list in two.  If number of elements is odd, right hand list is the longer one

sorted_list = [1,2,3,3,7,8,9,9]
number_to_find = 3
found_dict = {}
listoffset = 0

sorted_length = len(sorted_list)
listcenter = sorted_length/2

while (listcenter >= 1):

    listhalf1_len = int(listcenter)
    listhalf2_len = sorted_length - listhalf1_len
    
    listhalf1 = sorted_list[:listhalf1_len]
    listhalf2 = sorted_list[listhalf1_len:] 
    listhalf1_offset = listoffset
    listhalf2_offset = listoffset + listhalf1_len  
    
    # Check last element of lhl.  If number_to_find greater toss lhl 
    
    if (number_to_find < listhalf1[-1]):
        sorted_list = listhalf1
    elif (number_to_find > listhalf2[0]):
        sorted_list = listhalf2
        listoffset += listhalf1_len
    elif (number_to_find == listhalf1[-1]):
        found_dict [listoffset + listhalf1_len - 1] = number_to_find
        if listhalf1_len > 1:
            n = -2
            more_matches = True
            while (more_matches):
                if (number_to_find == listhalf1[n]):
                    found_dict [listoffset+ listhalf1_len + n ] = number_to_find
                    n -= 1
                else:
                    more_matches = False
                if n < -(listhalf1_len):
                    more_matches = False
        sorted_list = []
            
    elif (number_to_find == listhalf2[0]):
        listoffset += listhalf1_len
        found_dict [listoffset] = number_to_find
        if listhalf2_len > 1:
            n = 1
            more_matches = True
            while (more_matches):
                if ( number_to_find == listhalf2[n]):
                    found_dict [listoffset + n] = number_to_find
                    n += 1
                else:
                    more_matches = False
                if (n == listhalf2_len):
                    more_matches = False
        sorted_list = []
    else:
        sorted_list = []
        
    sorted_length = len(sorted_list)
    listcenter = sorted_length/2
