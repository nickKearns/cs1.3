#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]
        the time complexity of this function is O(1) constant time because for a linked list
        appending an item takes just a few actions that are not reliant on the number of entries
        in the linked list
        """
        # TODO: Push given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        this function takes constant time O(1) because accessing the head node of a linked
        list takes constant time. Traversing a linked list takes O(n) but because the target node is
        always the head node then it takes constant time
        """
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list.tail.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]
        This function takes O(n) time every time because the linked list's
        delete function is called to delete the node but that means that
        function call will traverse the entire linked list until it gets to 
        the tail. The LL delete function's worst case running time is O(n) and 
        the way it is being called here means it will always hit the worst
        case running time
        """
        # TODO: Remove and return top item, if any
        if self.list.tail:
            top_data = self.list.tail.data
            self.list.delete(top_data)
            return top_data
        else:
            raise ValueError("stack empty")


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]
        Time complexity for this function is O(1) because it takes constant time to 
        append something to a list
        """
        # TODO: Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        Time complexity is O(1) because accessing the index of a list is not effected
        by the number of elements in the list and it does not involve any loops so
        it is constant time
        """
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list[len(self.list) - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]
        The time complexity of this function is O(1) because the function only assigns an element of the list 
        to a variable which is constant time and then it calls the pop function of a list
        which takes constant time to run
        """
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError("stack empty")
        top_data = self.list[len(self.list) - 1]
        self.list.pop(len(self.list) - 1)
        return top_data


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
