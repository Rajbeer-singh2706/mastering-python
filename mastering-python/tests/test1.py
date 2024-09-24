import unittest

from ../modules import prob1_missing_number3

class TestFindMissingNumber(unittest.TestCase):

    # TestCase1
    def test_missing_number(self):
        input_list = [1,2,3,4,5]
        expected_output = [3]

        actual_output = prob1_missing_number3(input_list)
        self.assertEqual(actual_output, expected_output)


#python3 -m unittest test1.py
