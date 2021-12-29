"""
Given an integer n, return the total number of set bits in all integers between 1 and n (inclusive).

For example, given the n = 5, return 7 since we have the following numbers in binary:

i | binary
----------
1 | 001
2 | 010
3 | 011
4 | 100
5 | 101
And counting up all the 1s under the binary column gives us 7.

Bonus: Can you do this in O(log n) time?

Example 1
Input
n = 5

Output
7

Example 2
Input
n = 1

Output
1

Example 3
Input
n = 2

Output
2
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def dec_to_bin(num):
    l = []
    while num > 0:
        l.append(num % 2)
        num = num//2
    return l

def set_bits(n):
    c=0
    for i in range(0, n+1):
        c+=str(dec_to_bin(i)).count('1')
    return c


# DO NOT TOUCH THE BELOW CODE
class TestSetBits(unittest.TestCase):

    def test_01(self):
        self.assertEqual(set_bits(5), 7)

    def test_02(self):
        self.assertEqual(set_bits(1), 1)

    def test_03(self):
        self.assertEqual(set_bits(2), 2)

    def test_04(self):
        self.assertEqual(set_bits(0), 0)

    def test_05(self):
        self.assertEqual(set_bits(123), 424)

    def test_06(self):
        self.assertEqual(set_bits(896), 4291)

    def test_07(self):
        self.assertEqual(set_bits(2214), 12014)

    def test_08(self):
        self.assertEqual(set_bits(98424), 803466)


if __name__ == '__main__':
    unittest.main(verbosity=2)
