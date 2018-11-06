# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:50:30 2018

@author: Gautam Biswas
"""
"""
Implement a MyCalendarThree class to store your events. A new event can always be added.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all K events.)

For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there exists a K-booking in the calendar.

Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
Example 1:

MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
Explanation: 
The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
The remaining events cause the maximum K-booking to be only a 3-booking.
Note that the last event locally causes a 2-booking, but the answer is still 3 because
eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
 

Note:

The number of calls to MyCalendarThree.book per test case will be at most 400.
In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].
"""

"""
For a given call with an interval determine
if there is an intersection of points within
this interval with the intervals that already 
exist on the calendar.

Return the number of intersections that exist

There doesn't seem to be a built-in data element
to indicate range of a continuum of numbers, the 
mathematical equivalent of [ ](not a python list)
A tuple can be used but we would need another flag to indicate
whether to include the endpoints.  So I am creating
my own integer span object with a namedtuple.

I will use a flag on either end of the range. to indicate whether endpoints are included or not 

booking_time = (inc_left,10,12,inc_right)
calendar = [booking_time1,booking_time2...]
"""

from collections import namedtuple

calentry = namedtuple('meeting_time', 'inc_left start end inc_right')

meeting_10am = calentry(True,10,12,False)

## Write a class to check overlap of calendar entries.
calendar = []
calendar.append(meeting_10am)

def Check_Conflict(calentry,calendar):
    k = 1
    for element in calendar:
# check overlaps
        intersect = False
        if calentry.start < element.end:
            intersect = True
            k += 1
        elif calentry.end < element.start:
            intersect = True
            k += 1
    return k

meeting_11am = calentry(True,11,12,False)
Check_Conflict (meeting_11am,calendar)
            

"""

Solution from LeetCode

For each call to the method MyCalendar.book, 
return an integer K representing the largest integer 
such that there exists a K-booking in the calendar.


"""
import collections
class MyCalendarThree(object):

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1
        print (self.delta)

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active

        return ans
 
calendar = MyCalendarThree()
calendar.book(10,13)
calendar.book(9,11)
calendar.book(14,16)
"""
Another problem from LeetCode

N couples sit in 2N seats arranged in a row and 
want to hold hands. We want to know the minimum 
number of swaps so that every couple is sitting 
side by side. A swap consists of choosing any 
two people, then they stand up and switch seats.

The people and seats are represented by an integer 
from 0 to 2N-1, the couples are numbered in order, 
the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being 
the value of the person who is initially sitting in 
the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1])
 and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by 
side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""
