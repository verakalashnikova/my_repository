import unittest
import collections
from collections import defaultdict


class Strings(unittest.TestCase):

    def test_find_the_second_largest_element(self):
        """ Find the second frequent symbol in the string"""
        str = "vera is working right now. veraaaaa is aaaaa ggggggood gggggirl.............."
        string_map = self.create_my_map(str)
        print string_map
        self.find_the_second_largest_element(string_map)

    def create_my_map(self, str):
        my_map = {}
        if str:
            for symbol in str:
                if my_map.get(symbol):
                    my_map[symbol] += 1
                else:
                    my_map[symbol] = 1
            return my_map
        else:
            return None


    def find_the_second_largest_element(self, my_map):

        first_largest_element, first_largest_element_index = self.find_frequent_element(my_map)
        print "element = %s" % first_largest_element
        print "index = %s" % first_largest_element_index
        my_map[first_largest_element] = -1

        second_largest_element, second_largest_element_index = self.find_frequent_element(my_map)
        print "second element = %s" % second_largest_element
        print "second index = %s" % second_largest_element_index

        element_position_in_map = my_map.keys().index(second_largest_element)
        element_index = my_map[second_largest_element]

    def find_frequent_element(self, my_map):
        first_largest_element = None
        first_largest_element_index = -1

        for each_key in my_map:
            if first_largest_element is None:
                first_largest_element = each_key
                first_largest_element_index = my_map[each_key]
            else:
                if first_largest_element_index < my_map[each_key]:
                    first_largest_element_index = my_map[each_key]
                    first_largest_element = each_key
        return first_largest_element, first_largest_element_index

    def find_the_second_largest_element_1(self, my_map):
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

    def test_print_duplicate_caracters(self):
        """ 1. create a map of charaters with amount of its entrances in the str"""
        str = "averea"
        my_map = {}
        list_of_duplicate_characters = []
        for each_character in str:
            if not my_map.get(each_character, None):
                my_map[each_character] = 1
            else:
                my_map[each_character] += 1
        print "my_map =%s" % my_map

        for each_element in my_map:
            if my_map[each_element] == 2:
                list_of_duplicate_characters.append(each_element)

        print "list_of_duplicate_characters =%s" % list_of_duplicate_characters

    def test_check_if_two_strings_are_anograms_of_each_other(self):
        str1 = "vera"
        str2 = "arev"
        temp_str = ''
        for i in range(len(str1)):
            temp_str = temp_str + str1[len(str1)-1-i]
        print "temp_str = %s" % temp_str
        if temp_str == str2:
            print "str1 is anogram of str2"
        else:
            print "str1 is not anogram of str2"



    def test_print_first_non_repeated_character_from_the_string(self):
        str = "aveerrav"
        my_map = {}
        for each_character in str:
            if not my_map.get(each_character, None):
                my_map[each_character] = 1
            else:
                my_map[each_character] += 1

        for each_element in my_map:
            if my_map[each_element] == 1:
                print "first non repeated symbol is '%s'" % each_element
                break
            elif my_map[each_element] <> 1 and my_map.keys().index(each_element) ==(len(
                    my_map)-1):
                print "Non repeated symbol is not found"


    def test_recursion(self):
        str = "string"
        length = self.length_recursion(str)
        print "length = %s" % length

    def length_recursion(self, str):
        if str == '': return 0
        else:
            return 1 + self.length_recursion(str[:-1])

    def test_how_to_reverse_string_using_iteration(self):
        str = "vera1983"
        print str
        reversable_string = ""
        # for i in range(len(str)):
        #     reversable_string = reversable_string + str[len(str)-1-i]
        for each_symbol in str[::-1]:
            reversable_string = reversable_string + each_symbol
        print "reversable string is = %s" % reversable_string

    def test_how_to_reverse_string_using_recursion(self):
        str = "vera"
        print "str=%s" % str
        #str[-1:] to take the last symbol
        reverse_str = self.reverse_string_rec(str)
        print "reverse_str=%s" % reverse_str

    def reverse_string_rec(self, string):
        if string=='': return string
        else:
            return self.reverse_string_rec(string[1:]) + string[0]
            # print "my_map = %s" % my_map

    def test_count_vowels(self):
        str = "Vera is working"
        str = str.lower()
        # count = self.vowel_count(str)
        count = self.rec_vowel_count(str)
        print "count = %s" % count

    def rec_vowel_count(self, str):
        """ Count vowels in the string using recursion"""
        vowels = "aeiouAEIUO"
        if str == "":
            return 0
        elif str[0] in vowels:
            return 1 + self.rec_vowel_count(str[1:])
        else:
            return 0 + self.rec_vowel_count(str[1:])

    def vowel_count(self, str):
        """ Count vowels in ste string"""
        vowels = "aeiouAEIUO"
        counter = 0
        for symbol in str:
            if symbol in vowels:
                counter += 1

        return counter

    def test_polindrom_pairs(self):
        str1 = "vera"
        str2 = "arev"
        i = 0
        assert len(str1) == len(str2)

        for i in range(0, len(str1)):
            assert str1[i] == str2[len(str2)-i-1]

    def test_reverse_vowels_in_string(self):
        """ The method gets a string as an input and reverse only vowels
        1. create a map vowel - position in the string
        2. order the map
        3. reverse vowels
        """
        str = "vera is a girl"
        expected_str = "vira is a gerl"
        vowels = "aeiouAEIUO"
        list_vowels_in_str = []
        vowels_map = {}
        for i in range(len(str)):
            if str[i] in vowels:
                list_vowels_in_str.append(str[i])
                vowels_map[i] = str[i]
                # vowels_map.
        print vowels_map
        print list_vowels_in_str
        sorted_vowels_map = collections.OrderedDict(sorted(vowels_map.items()))
        print sorted_vowels_map

        new_str = ""
        i = 0
        for each_char in str:
            if each_char in vowels:
                # replace vowels
                if i == 0:
                    index = sorted_vowels_map.keys()[-1]
                    print "index = %s" % index
                    print "element = %s" % sorted_vowels_map[index]
                    new_str = new_str + sorted_vowels_map[index]
                else:
                    index = sorted_vowels_map.keys()[-1-i:-i][0]
                    new_str = new_str + sorted_vowels_map[index]
                i += 1
            else:
                new_str += each_char
        print new_str
        assert expected_str == new_str

    def test_reverse_words_within_sentence(self):
        """ Given a string, you need to reverse the order of characters in each word within a
        sentence while still preserving whitespace and initial word order."""
        str = "vera is a good girl"
        expected_str = "arev si a doog lrig"
        words_list = str.split(' ')
        new_str = ""
        print words_list
        for index, each_word in enumerate(words_list):
            new_word = ""
            for i in range(len(each_word)):
                new_word += each_word[-1-i]
            new_str += new_word if index == 0 else (" " +new_word)

        self.assertEquals(expected_str, new_str)

    def test_reverse_string_recursion(self):
        str = "vera"
        reverse_str = self.rev_str_rec(str)
        print reverse_str

    def rev_str_rec(self, str):
        if str == '': return str
        else: return self.rev_str_rec(str[1:]) + str[0]


    def pangram_or_not(s):
        """ if s is a pangram returns True, otherway returns False"""
        my_map = {}
        if s is None:
            return False
        for each_symbol in s:
            if each_symbol.ifalpha():
                if my_map.get(each_symbol):
                    my_map[each_symbol] += 1
            else:
                my_map[each_symbol] = 1


        if len(my_map) == 26:
            return True
        else:
            return False

    def test_pangram(self):
        a1 = ord('a')
        a2 = ord('z')
        A1 = ord('A')
        A2 = ord('Z')
        lower_case_letters = ''
        upper_case_letters = ''
        for i in range(a1,a2+1):
            lower_case_letters += chr(i)

        upper_case_letters = lower_case_letters.upper()
        print lower_case_letters
        upper_case_letters = lower_case_letters.upper()
        print upper_case_letters


    def test_find_all_friends(self):
        employee = [
            "1, Name1, employee1",
            "2, Name2, employee2",
            "3, Name3, employee3",
            "4, Name4, employee4",
            "5, Name5, employee5",
            "6, Name6, employee6",
            "7, Name7, employee7",
            "8, Name8, employee8",
            "9, Name9, employee9",
        ]
        friend_map = [
            "1,2",
            "1,3",
            "1,4",
            "2,3",
            "3,1",
            "4,6",
            "5,7"
        ]

        employee_ids_list = []
        for each in employee:
            employee_id = each.split(",")[0]
            employee_ids_list.append(employee_id)

        # print "ids list is %s" % employee_ids_list

        # initialize keys for my_friends_map using employee_ids_list
        my_friend_map = defaultdict(list)
        for each_id in employee_ids_list:
            my_friend_map[each_id] = []


        for each in friend_map:
            each_record = each.split(',')
            # if my_friend_map.get(each_record[0]) is None:
            my_friend_map[each_record[0]].append(each_record[1])
            # else:
            #     my_friend_map.get(each_record[0]).append(each_record[1])
            my_friend_map[each_record[1]].append(each_record[0])

        print "my_friend_map = %s" % my_friend_map

if __name__ == '__main__':
    unittest.main()


    # def test_vera(self):
    #     loans = []
    #     records = self.writeoff_queries.get_loc_eligible_for_writeoff()
    #     for each_record in records:
    #         loan_id = each_record["loan_id"]
    #         loans.append(loan_id)
    #
    #     print loans
    #     print len(loans)
    #     my_loans = []
    #     for loan_id in loans:
    #         record = self.servicing_transaction_queries.get_transactions_for_loc_activity(loan_id)[
    #             0]
    #         if record["state"] == 'PENDING':
    #             my_loans.append(loan_id)
    #
    #     print my_loans
    #     print len(my_loans)
    #########
    # def move_dates_for_just_boarded_loan(self, new_date, loan_id):
    #     sql = """
    #         update commitment_transactions
    #         set transaction_date='%s'
    #         where loan_id = '%s'
    #         """ % (new_date, loan_id)
    #     response = self.odc_postgres.execute_odc_query(sql)[0]
    #     return response
    #
    #
    # def move_dates_for_reissued_loan(self, new_date, new_payment_date, loan_id):
    #     sql = """
    #         update commitment_transactions
    #         set transaction_date='%s', open_date='%s', next_payment_date='%s'
    #         where loan_id = '%s'
    #         """ % (new_date, new_date, new_payment_date, loan_id)
    #     response = self.odc_postgres.execute_odc_query(sql)[0]
    #     return response
    #
    #
    # def move_dates_after_put_on_hold(self, new_date, loan_id):
    #     sql = """
    #         update commitment_transactions
    #         set hold_date='%s'
    #         where loan_id = '%s'
    #         """ % (new_date, loan_id)
    #     response = self.odc_postgres.execute_odc_query(sql)[0]
    #     return response
    #
    #
    # def move_dates_after_closing(self, new_date, loan_id):
    #     sql = """
    #         update commitment_transactions
    #         set closed_date='%s'
    #         where loan_id = '%s'
    #         """ % (new_date, loan_id)
    #     response = self.odc_postgres.execute_odc_query(sql)[0]
    #     return response
    #
    #
    # def update_dates_for_transactions(self, new_date, transaction_set_id):
    #     sql = """
    #         update loan_transaction set sentdate='%s', clear_processor_date='%s',
    #         clear_bank_date = '%s', clear_funding_source_date='%s'
    #         where transaction_set_id in (%s)
    #         """ % (new_date, new_date, new_date, new_date, transaction_set_id)
    #     response = self.odc_postgres.execute_odc_query(sql)[0]
    #     return response
    #
    #
    # def update_dates_for_reissue(self, new_date, loan_reissue_id):
    #     sql = """
    #         update loan_reissue
    #         set created_date='%s', updated_date = '%s'
    #         where loan_reissue_id = '%s'
    #         """ % (new_date, new_date, loan_reissue_id)
    #     response = self.odc_postgres.execute_odc_query(sql)[0]
    #     return response