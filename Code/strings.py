#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    
    This functions time complexity is based directly off of find_all_indexes()
    time complexity. The worst case is that two for loops must be iterated over completely
    the outer for loop being iterated completely means that the inner one is iterated over how 
    ever many times the outer one is so it is multiplicative
    Therefore the time complexity is O(n*m)
    n being the number of elements in the text parameter to be iterated over in the outer for loop
    and m being the number of elements in the pattern parameter to iterated over in the inner for loop
    
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)


    # for i in range(len(text)):
    #     match = True
    #     for j in range(len(pattern)):
    #         if text[i+j] != pattern[j]:
    #             match = False
    #             break
    #     if match:
    #        return match
    # return False
    if find_all_indexes(text, pattern):
        return True
    else:
        return False

    




def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    
    Worst case time complexity is O(n*m)
    Because the find_all_indexes() function is being used this function's
    time complexity is based directly off of that functions complexity
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    # for i in range(len(text)):
    #     match = True
    #     for j in range(len(pattern)):
    #         if text[i+j] != pattern[j]:
    #             match = False
    #             break
    #     if match:
    #         return i
    # return None
    list_of_occurances = find_all_indexes(text, pattern)
    if list_of_occurances:
        return list_of_occurances[0]
    else:
        return None




        


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    
    Time Complexity: Best case time complexity is that there is no pattern inputed,
    which would just be an empty string and that matches the entire text string so
    this function will return just the length of the text inputed
    Worst case is O(n*m) because it is a double for loop that loops through 
    the length ofthe text(n) and the length of the pattern(m). The worst case is that the 
    function has to loop through both for loops entirely, meaning that it for every n iteration 
    of the outter for loop m was iterated over completely, so that is where the n * m comes from
    This functions time complexity heavily effects the above two functions' time complexities

    
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    if not pattern:
        return [i for i in range(len(text))]


    list_of_indexes = []
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            list_of_indexes.append(i)
    return list_of_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
