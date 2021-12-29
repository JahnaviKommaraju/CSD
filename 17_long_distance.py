"""
Given an array of integers, return a new array where each element
in the new array is the number of smaller elements to the right
of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
Bonus: Can you do this in O(n log n) time?

Example 1
Input

lst = [3, 4, 9, 6, 1]
Output

[1, 1, 2, 1, 0]
Example 2
Input

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Output

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Example 3
Input

lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Output

[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def long_distance(lst):
    if lst==[]:
        return []
    arr=[]
    for i in range(len(lst)-1):
        c=0
        for j in range(i+1,len(lst)):
            if (lst[j]<lst[i]):
                c+=1
        arr.append(c)
    arr.append(0)
    return arr


# DO NOT TOUCH THE BELOW CODE
class TestLongDistance(unittest.TestCase):

    def test_01(self):
        self.assertEqual(long_distance([3, 4, 9, 6, 1]), [1, 1, 2, 1, 0])

    def test_02(self):
        self.assertEqual(long_distance([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_03(self):
        self.assertEqual(long_distance([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
                         [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_04(self):
        self.assertEqual(long_distance([]), [])

    def test_05(self):
        self.assertEqual(long_distance([18, 2, 16, 6, 5, 2, 19, 19, 13]),
                         [6, 0, 4, 2, 1, 0, 1, 1, 0])

    def test_06(self):
        self.assertEqual(long_distance([10, 15, 20, 23, 14, 20, 16, 10, 10, 15, 19, 18, 16, 10, 23, 12, 24, 10, 23, 19, 20, 10,
                                        11, 20, 25, 20, 10, 14, 20, 25, 13, 18, 23, 25, 11, 11, 10, 17, 11, 25, 13, 15, 16, 11, 10, 12, 24, 11, 12, 12]),
                         [0, 22, 32, 37, 20, 31, 23, 0, 0, 19, 25, 23, 20, 0, 27, 11, 28, 0, 25, 20, 20, 0, 3, 18, 22, 18, 0, 12, 16, 18, 10, 14, 14, 15, 2, 2, 0, 10, 1, 10, 6, 6, 6, 1, 0, 1, 3, 0, 0, 0])

    def test_07(self):
        self.assertEqual(long_distance([34, 36, 30, 15, 32, 26, 2, 7, 39, 9, 14, 35, 12, 40, 24, 15, 14, 11, 36, 24, 39, 2, 32, 8, 31, 39, 7, 18, 2, 34, 20, 16, 30, 2, 31, 27, 7, 4, 24, 26, 36, 20,
                                        4, 29, 23, 20, 8, 13, 20, 39, 9, 37, 15, 6, 19, 28, 1, 28, 25, 19, 14, 22, 12, 40, 4, 23, 36, 36, 11, 28, 5, 21, 30, 22, 7, 15, 16, 12, 21, 4, 22, 17, 4, 20, 26, 34, 15, 3, 5, 24]),
                         [74, 77, 67, 31, 70, 58, 1, 13, 76, 18, 25, 68, 21, 75, 48, 26, 24, 19, 63, 45, 66, 1, 58, 15, 55, 62, 12, 27, 1, 53, 28, 23, 48, 1, 48, 42, 10, 2, 35, 37, 44, 24, 2, 39, 31, 23, 9, 13, 21, 39, 9, 37, 13, 7, 16, 27, 0, 26, 24, 15, 10, 17, 8, 26, 1, 17, 22, 22, 6, 18, 3, 11, 16, 12, 4, 5, 6, 4, 7, 1, 6, 4, 1, 3, 4, 4, 2, 0, 0, 0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
