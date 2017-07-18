import unittest

class Files(unittest.TestCase):

    def test_reverse_words_within_file(self):
        """
         1. input: file_name
         2. Read 60 bites from the file
         3. Reverse words in this piece
         4. Read the next 60 bites and so on
        """
        file_name = '1.txt'
        with open(file_name) as f:
            content = f.readlines(64)
        print content
