#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)



def linear_search_iterative(array, item):
    # loop over all array values until item is found
    '''The time complexity of this function in O(n) because the function must search through each element in the array. O(n) is the worst case O(1) 
    is the best case.'''
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    '''The time complexity of this function is O(n) because with each recursive call of the function it is searching through a single item
    but the number of times the function is called is dependent on the length of the array or the number n entries in the array so the time complexity is 
    O(n). O(n) is the worst case and O(1) is the best case'''


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
    '''The time complexity of this function is O(log2(n)) because with every iteration of the while loop the total number of 
    entries or n to be searched through is half that of the previous iteration. O(log2(n)) is the average case time complexity while O(1) is
    the best case time complexity'''





    lower_bound = 0
    upper_bound = len(array) - 1
    mid_bound = (lower_bound + upper_bound) // 2

    while not array[mid_bound] == item:
        if item > array[mid_bound]:
            lower_bound = mid_bound + 1
            mid_bound = (lower_bound + upper_bound) // 2



        elif item < array[mid_bound]:
            upper_bound = mid_bound - 1
            mid_bound = (lower_bound + upper_bound) // 2


        if lower_bound == mid_bound and array[lower_bound] != item:
            return None
    return mid_bound

    

    
    




def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    '''The time complexity of this function is O(log2(n)) similar to the non recursive binary search function but instead of having a while loop
    this function just calls itself recursively until the search has ended. This function also splits the number of n entries it has to search through
    with each call of itself so as the recursion develops the number of entries to be searched is being cut in half each time.
    O(log2(2)) is the average case time complexity while O(1) is the best case time complexity.'''

    if left == None and right == None:
        left = 0
        right = len(array) - 1
   

    mid_bound = (left + right) // 2


    
    if array[mid_bound] == item:
        return mid_bound
    elif left == mid_bound and array[left] != item:
        return None
    else:
        if item > array[mid_bound]:
            left = mid_bound + 1
        else:
            right = mid_bound - 1
        return binary_search_recursive(array, item, left, right)




