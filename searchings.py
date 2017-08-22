""" Given an array arr[] of n elements. Find a given element x using each searching"""
import unittest


class Searching(unittest.TestCase):
    def setUp(self):
        self.arr = [5,8,3,1,6,9,11,15,2]
        self.x = 15

    def test_linear_serching(self):
        for i in range(len(self.arr)):
            if self.arr[i] == self.x:
                print self.arr.index(self.arr[i])
                return self.arr.index(self.arr[i])
        return -1

