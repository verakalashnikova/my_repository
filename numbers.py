import unittest
import pprint
from array import array

class Numbers(unittest.TestCase):

    def test_selection_sort(self):
        """ The selection sort algorithm sorts an array by repeatedly finding the minimum element
        from unsorted part and put it to the biginning. The algorithm maintains 2 subarrays in a
        given array"""
        my_array = [64, 25, 12, 22, 11]
        for i in range(len(my_array)):
            min_index = i
            for j in range(i+1, len(my_array)):
                if my_array[j] < my_array[min_index]:
                    min_index = j
            my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
        print my_array

    def test_max_product_of_3_numbers(self):
        """ Given an integer array, find three numbers whose product is maximum and output the
        maximum product. """
        arr = [1,5,7,8,2,9,11,15,4]
        max = -1
        arr_of_max = []
        for i in range(0,3):
            max = self.find_max_element(arr)
            arr_of_max.append(max)
            index = arr.index(max)
            arr[index] = -100

        result = 1
        for element in arr_of_max:
            result = result * element
        print result

    def find_max_element(self, arr):
        """ Accepts an array of numbers. Returns max element from the
        array which less than the given max element"""
        curr_max = arr[0]
        for element in arr:
            if element > curr_max:
                curr_max = element
        return curr_max


    def test_find_values(self):
        """ Find all values in a list of integers that sum equals k """

        my_array = [1,2,4,5,3]
        k = 5
        values = []
        for i in range(len(my_array)):
            for j in range(i+1, len(my_array)):
                sum = my_array[i] + my_array[j]
                if sum == k:
                    val = [my_array[i], my_array[j]]
                    values.append(val)
        pprint.pprint(values)


    def test_sorting_large_small(self):
        """ Sort an unsorted array the first element is the largest number, the second is the
        smallest, the third is the second largest number and so on."""
        my_array = [5,2,6,9,1,4,3]
        # expected_sorted_array = [9,1,5,2,4,3]
        sorted_array = []

        # Sort array from the smallest to the largest.
        # min_element = 0
        # for current_number in my_array:
        #     if current_number > min_element:
        # array.

        # Off the shelf sorting algorithm.

