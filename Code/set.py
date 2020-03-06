
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
        return self.table.contains(item)


    def add(self, item):
        if self.contains(item) == False:
            self.table.set(item, 1) #there are no real values for the key value pair so im gonna default it to 1


    def delete(self, item):
        self.table.delete(item)


    def union_op(self, set_b):
        '''

        .keys() call takes O(n) time every time so that would be 2*n 
        

        '''
        set_c = Set(self.table.keys() + set_b.table.keys())
        return set_c
        

    def intersection_op(self, set_b):
        '''
        
        '''


        set_c_list = []
        for item in self.table.keys():
            if set_b.contains(item):
                set_c_list.append(item)
        return Set(set_c_list)

    
    def difference_op(self, set_b):
        set_c = Set()
        for item in self.table.keys():
            if not set_b.contains(item):
                set_c.add(item)
        return set_c


    def is_subset_op(self, set_b):
        '''
        returns a boolean on whether or not set a is a subset of the given set
        O(m*n) or O(n^2)
        '''
        counter = 0
        for item in self.table.keys():
            if set_b.contains(item):
                counter += 1

        return counter == self.size()
