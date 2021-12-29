"""
Given an integer n, we apply this transformation until it
becomes a 1: take each of the digits in n, square it, and
then take their sum.

Return whether n will end up in 1 after the transformations.

Example 1
Input
n = 7

Output
True

Explanation
This is a happy number since we get this sequence [49, 97, 130, 10, 1]

7 ** 2 = 49
4 ** 2 + 9 ** 2 = 97
9 ** 2 + 7 ** 2 = 130
1 ** 2 + 3 ** 2 + 0 ** 2 = 10
1 ** 2 + 0 ** 2 = 1

Example 2
Input
n = 11

Output
False

Explanation
This is not a happy number since it ends up in a cycle: [2, 4, 16, 37, 58, 89, 145, 42, 20, 4]

2 ** 2 = 4
4 ** 2 = 16
1 ** 2 + 6 ** 2 = 37
3 ** 2 + 7 ** 2 = 58
5 ** 2 + 8 ** 2 = 89
8 ** 2 + 9 ** 2 = 145
1 ** 2 + 4 ** 2 + 5 ** 2 = 42
4 ** 2 + 2 ** 2 = 20
2 ** 2 + 0 ** 2 = 4
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def happy_numbers(n):
    while True:
        n = sum([int(i) ** 2 for i in str(n)])
        if n == 1:
            return True
        if n == 4:
            return False


# DO NOT TOUCH THE BELOW CODE
class TestHappyNumbers(unittest.TestCase):

    def test_01(self):
        self.assertEqual(happy_numbers(7), True)

    def test_02(self):
        self.assertEqual(happy_numbers(11), False)

    def test_03(self):
        self.assertEqual(happy_numbers(145), False)

    def test_04(self):
        self.assertEqual(happy_numbers(435), False)

    def test_05(self):
        self.assertEqual(happy_numbers(784), True)

    def test_06(self):
        self.assertEqual(happy_numbers(1857), True)

    def test_07(self):
        self.assertEqual(happy_numbers(5551), False)

    def test_08(self):
        self.assertEqual(happy_numbers(43560), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
