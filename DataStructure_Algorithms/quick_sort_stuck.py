#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:49:34 2020

@author: clairegong
"""

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quick_sort(array):

    if len(array) == 1:
        return

    end = len(array) - 1
    pivot = 0
    temp_idx = 1
    for i in range(pivot+1, end):
        if array[i] < array[pivot]:
            array[i], array[temp_idx] = array[temp_idx], array[i]
            temp_idx += 1
    array[pivot], array[temp_idx - 1] = array[temp_idx - 1], array[pivot]

    quick_sort(array[:temp_idx-1])
    quick_sort(array[temp_idex+1:])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quick_sort(test))

# reference pseudocode
# for each (unsorted) partition
# set first element as pivot
#   storeIndex = pivotIndex + 1
#   for i = pivotIndex + 1 to rightmostIndex
#     if element[i] < element[pivot]
#       swap(i, storeIndex); storeIndex++
#   swap(pivot, storeIndex - 1)

