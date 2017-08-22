import unittest
from array import array


class Sortings(unittest.TestCase):

    def test_selection_sort(self):
        """ The selection sort algorithm sorts an array by repeatedly finding the minimum element
        (considering ascending order) from unsorted part and put it at the beginning"""
        arr = [5,8,1,4,9,3,6]
        for i in range(len(arr)):
            min = i
            for j in range(len(arr)):
                if arr[j] > arr[min]:
                    arr[j],arr[min] = arr[min],arr[j]

        print arr


    def test_bubble_sort(self):
        """ Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the
        adjacent elements if they're in wrong order """
        arr = [5, 8, 1, 4, 9, 3, 6]
        for i in range(len(arr)):
            print "i= %s, arr=%s" % (i, arr)
            for j in range(len(arr)-i-1):
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]

        print arr