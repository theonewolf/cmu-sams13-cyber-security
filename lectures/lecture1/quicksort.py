#!/usr/bin/env python

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)/2]; del array[len(array)/2]
    less = []; greater = []
    for x in array:
        if x <= pivot: less.append(x)
        else: greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)

# test the quicksort function if executed directly
if __name__ == '__main__':
    print quicksort([1,9,4,3,5,6,7,23,34,8,9])
