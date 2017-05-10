import unittest


class Strings(unittest.TestCase):

    def test_find_the_second_largest_element(self):
        """ Find the second frequent symbol in the string"""
        str = "veraa is working right now. veraaaaaa is a good girllllllllll"
        string_map = self.create_map(str)
        self.find_the_second_largest_element(string_map)

    def create_map(self,str):

        my_map = {}
        for each_char in str:
            if not my_map.get(each_char, None):
                my_map[each_char] = 1
            else:
                my_map[each_char] += 1

        print("list =%s" % my_map)
        return my_map

    def find_the_second_largest_element(self, my_map):
        """ The method finds the first largest element and replace it on -1000000 """
        first_max_element = None
        first_max_element_index = -1
        for each_element in my_map:
            if not first_max_element:
                first_max_element = my_map[each_element]
                first_max_element_index = my_map.keys().index(each_element)
            if my_map[each_element] > first_max_element:
                first_max_element = my_map[each_element]
                first_max_element_index = my_map.keys().index(each_element)
        first_max = my_map.keys()[first_max_element_index]
        print "first_max = %s" % first_max
        my_map[first_max] = -1

        print "first_max_element_index =%s" % first_max_element_index
        second_max_element = None
        second_max_element_index = -1
        for each_element in my_map:
            if not second_max_element:
                second_max_element = my_map[each_element]
                second_max_element_index = my_map.keys().index(each_element)
            if my_map[each_element] > second_max_element and my_map[
                each_element] < first_max_element:
                second_max_element = my_map[each_element]
                second_max_element_index = my_map.keys().index(each_element)

        second_max = my_map.keys()[second_max_element_index]
        print "second_max = %s" % second_max

        print "second_max_element_index =%s" % second_max_element_index
        print ("first_max_element =%s" % first_max_element)
        print ("second_max_element =%s" % second_max_element)

if __name__ == '__main__':
    unittest.main()