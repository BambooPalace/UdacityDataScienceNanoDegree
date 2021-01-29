#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:49:34 2020

@author: clairegong
"""

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    unsorted = array#extra space..how do i mark an element as sorted?
    #how do i slice the array to be sorted
    
    pivot = 0
    temp_idx = 1
    for i in range(1,len(unsorted)):
        if unsorted[i] < array[pivot]:
            unsorted[i], unsorted[temp_idx] = unsorted[temp_idx],unsorted[i]
            temp_idx += 1
    unsorted[pivot], unsorted(temp_idx-1) = unsorted(temp_idx-1),unsorted[pivot]
    
    
    
    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))

#reference pseudocode
# for each (unsorted) partition
# set first element as pivot
#   storeIndex = pivotIndex + 1
#   for i = pivotIndex + 1 to rightmostIndex
#     if element[i] < element[pivot]
#       swap(i, storeIndex); storeIndex++
#   swap(pivot, storeIndex - 1)

