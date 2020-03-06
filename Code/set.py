
from hashtable import HashTable


class Set:
    def __init__(self, items=None):
        self.table = HashTable()
        if items:
            for item in items:
                self.add(item)


    def size(self):
        return self.table.length()

    def contains(self, item):
        '''
        This takes O(1) time complexity because this set class is
        implemented with a hash table which has constant time lookup 
        '''
        return self.table.contains(item)


    def add(self, item):
        '''
        Time complexity = O(1), this function calls the self.contains function which is O(1)
        and then it calls table.set which for hash tables takes constant time almost every time
        the exception is when the hash table needs to be resized to lower its load factor
        '''
        if self.contains(item) == False:
            self.table.set(item, 1) #there are no real values for the key value pair so im gonna default it to 1


    def delete(self, item):
        '''
        Time complexity = O(1) because this function calls on the hash tables
        delete function which takes constant time because it can use the hash function
        to find the correct bucket immediately and then if the load factor
        of the hash table is low, which it always should be, then traversing that linked list
        within that bucket would take constant time as well
        '''

        self.table.delete(item)


    def union_op(self, set_b):
        '''

        .keys() call takes O(n) time every time so that would be 2*n because 
        it is called on self and set_b.
        The Set initializer calls on the self.add() function which takes O(1).
        so time complexity is O(n)
        

        '''
        set_c = Set(self.table.keys() + set_b.table.keys())
        return set_c
        

    def intersection_op(self, set_b):
        '''
        self.table.keys() takes O(n) because it returns every element in the hashtable
        set_c_list.append(item) takes O(1) because adding to a list is constant time
        so this function takes O(n)
        '''


        set_c_list = []
        for item in self.table.keys():
            if set_b.contains(item):
                set_c_list.append(item)
        return Set(set_c_list)

    
    def difference_op(self, set_b):
        '''
        .keys() call takes O(n)
        .contains() takes O(1) because it is constant look up time for
        a hash table
        .add() function takes constant time
        overall time complexity = O(n)
        '''
        set_c = Set()
        for item in self.table.keys():
            if not set_b.contains(item):
                set_c.add(item)
        return set_c


    def is_subset_op(self, set_b):
        '''
        returns a boolean on whether or not set a is a subset of the given set
        The for loop iterates over all the elements in self.table so that is O(n)
        set_b.contains is called every iteration which is n times so we could say
        that the time complexity is O(n^2)
        '''
        counter = 0
        for item in self.table.keys():
            if set_b.contains(item):
                counter += 1

        return counter == self.size()
