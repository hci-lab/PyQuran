"""unittest module for searchHelper.py
"""
import unittest

from searchHelper import *
class Testing_searchHelper(unittest.TestCase):

    def test_count_spaces_before_index(self):
        self.assertEqual(count_spaces_before_index('', 0), 0)
        self.assertEqual(count_spaces_before_index('01 34 6 8', 8), 3)
        self.assertEqual(count_spaces_before_index(' ', 1), 1)


if __name__ == '__main__':
    unittest.main()
