import unittest
import time

class Files(unittest.TestCase):

    def test_reverse_words_within_file(self):
        """
         1. input: file_name
         2. Read 64 bites from the file
         3. Reverse words in this piece
         4. Read the next 60 bites and so on
        """
        t = (int(time.time()))
        t = str(t)
        file_name = '1.txt'
        with open(file_name) as f: # Get a file object
            with open(t+f.name, 'wr') as f_new:
                while True:
                    str1 = self.read_in_chunks(f)
                    if not str1:
                        break
                    print str1
                    curr_position_in_file = f.tell()
                    # if element in the current position is not space we need to move back to space
                    # and read from that position
                    char = str1[-1]
                    counter = 0
                    while char != ' ' and char != '\n':
                        counter += 1
                        char = str1[-1-counter]
                    # change str
                    if counter != 0:
                        str1 = str1[:-counter]
                        print str1
                    new_str = self.revert_words_in_string(str1)
                    print new_str
                    f_new.write(new_str)
                    f.seek(curr_position_in_file - counter)

    def read_in_chunks(self, f, chunk_size=64):
        return f.read(chunk_size)

    def revert_words_in_string(self, str):
        self.assertIsNotNone(str)
        words_list = str.split(' ')
        new_str = ""
        print words_list
        for index, each_word in enumerate(words_list):
            new_word = ""
            for i in range(len(each_word)):
                new_word += each_word[-1 - i]
            new_str += new_word if index == 0 else (" " + new_word)
        return new_str
