from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        set_a = Set()
        assert set_a.size() == 0
        assert set_a.contains('A') == False
        assert set_a.contains(30) == False

    def test_contains(self):
        set_a = Set(['A', 'B', 'C', 'D'])
        assert set_a.contains('B') == True
        assert set_a.contains('b') == False
        assert set_a.contains('D') == True
        assert set_a.size() == 4


    def test_add(self):
        set_a = Set()
        set_a.add('A')
        assert set_a.contains('A') == True
        assert set_a.contains('a') == False
        set_a.add('K')
        assert set_a.contains('K') == True
        assert set_a.size() == 2
        


    def test_delete(self):
        set_a = Set(['A', 'B', 'C', 'D'])
        assert set_a.contains('A') == True
        set_a.delete('A')
        assert set_a.size() == 3
        assert set_a.contains('A') == False
        assert set_a.contains('C') == True
        
        
    
    def test_union(self):
        set_a = Set([1, 3, 5, 7])
        set_b = Set([2, 4, 6])
        set_c = set_a.union_op(set_b)
        assert set_c.contains(1) == True
        assert set_c.contains(2) == True
        assert set_c.contains(8) == False
        set_c.delete(5)
        assert set_c.contains(5) == False


    def test_intersection(self):
        set_a = Set([1, 3, 5, 7])
        set_b = Set([2, 3, 4, 6, 7])
        set_c = set_a.intersection_op(set_b)
        assert set_c.contains(1) == False
        assert set_c.contains(7) == True
        assert set_c.contains(3) == True
        assert set_c.contains(4) == False


    def test_difference(self):
        set_a = Set([1,4,6,8,10])
        set_b = Set([1,6,10])
        set_c = set_a.difference_op(set_b)
        assert set_c.contains(1) == False
        assert set_c.contains(4) == True


    def test_is_subset(self):
        set_a = Set([1,4,6,8,10])
        set_b = Set([1,4,8,10])
        assert set_b.is_subset_op(set_a) == True
        assert set_a.is_subset_op(set_b) == False