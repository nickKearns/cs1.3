#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]
        this function takes constant time because appending something to a linked list takes constant time
        """
        # TODO: Insert given item
        self.list.prepend(item)
        

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty.
        """
        # TODO: Return front item, if any
        if self.list.is_empty():
            return None
        else:
            return self.list.tail.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]
        This function takes constant time because the linked list delete function is called
        and that functions best case run time is O(1) and that is always the case with 
        how it is being called here because the node being deleted is always the first
        node checked
        """
        # TODO: Remove and return front item, if any
        if self.list.is_empty():
            raise ValueError("no data")
        else:
            front_data = self.list.tail.data
            self.list.delete(front_data)
            return front_data

        


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]
        This takes constant time because appending something to a list takes constant time
        """
        # TODO: Insert given item
        self.list.append(item)


    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list[0]


    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]
        This function's time complexity is O(n) because when you delete an element 
        from a list all the things after it must be shifted down in memory so 
        the time complexity is dependent on the number of items after what is being
        deleted and since what is being deleted is the first element then n number of 
        items are being shifted
        """
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError("queue is empty")
        front_data = self.list[0]
        self.list.pop(0)
        return front_data

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
