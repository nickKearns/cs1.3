#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    if index >= len(array):
        return None
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
    



def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    lower_bound = 0
    upper_bound = len(array)
    mid_bound = (lower_bound + upper_bound) // 2

    while not array[mid_bound] == item:
        if item > array[mid_bound]:
            lower_bound = mid_bound
            mid_bound = (lower_bound + upper_bound) // 2



        elif item < array[mid_bound]:
            upper_bound = mid_bound
            mid_bound = (lower_bound + upper_bound) // 2


        if (lower_bound == mid_bound or upper_bound == mid_bound) and array[lower_bound] != item:
            return None
    return mid_bound

    

    
    




def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    if left == None and right == None:
        lower_bound = 0
        upper_bound = len(array)
    else:
        lower_bound = left
        upper_bound = right

    mid_bound = (lower_bound + upper_bound) // 2


    
    if array[mid_bound] == item:
        return mid_bound
    elif lower_bound == mid_bound and array[lower_bound] != item:
        return None
    else:
        if item > array[mid_bound]:
            lower_bound = mid_bound
        else:
            upper_bound = mid_bound
        return binary_search_recursive(array, item, lower_bound, upper_bound)