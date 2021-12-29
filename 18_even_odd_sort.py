"""
Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order
The relative positions of the even and odd numbers remain the same

Example 1
Input
nums = [8, 13, 11, 90, -5, 4]

Output
[4, 13, 11, 8, -5, 90]

Explanation
The even numbers are sorted in increasing order, the odd numbers are sorted in decreasing number,
and the relative positions were [even, odd, odd, even, odd, even] and remain the same after sorting.
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def even_odd_sort(nums):
    l=nums
    fl=[]
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort(reverse=True)
    i=0
    j=0
    for _ in range(len(l)):
        if l[_]%2==0:
            fl.append(even[i])
            i+=1
        else:
            fl.append(odd[j])
            j+=1
    return fl


# DO NOT TOUCH THE BELOW CODE
class TestEvenOddSort(unittest.TestCase):

    def test_01(self):
        self.assertEqual(even_odd_sort(
            [8, 13, 11, 90, -5, 4]), [4, 13, 11, 8, -5, 90])

    def test_02(self):
        self.assertEqual(even_odd_sort([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])

    def test_03(self):
        self.assertEqual(even_odd_sort(
            [18, 2, 16, 6, 5, 2, 19, 19, 13]), [2, 2, 6, 16, 19, 18, 19, 13, 5])

    def test_04(self):
        self.assertEqual(even_odd_sort(
            [39, 40, 16, 21, 34, 21, 32, 4, 39, 34, 29, 8, 16, 13, 1, 9, 11, 3, 39, 25]),
            [39, 4, 8, 39, 16, 39, 16, 32, 29, 34, 25, 34, 40, 21, 21, 13, 11, 9, 3, 1])

    def test_05(self):
        self.assertEqual(even_odd_sort([364, 605, 589, 444, 916, 802, 294, 336, 807, 707]),
                         [294, 807, 707, 336, 364, 444, 802, 916, 605, 589])

    def test_06(self):
        self.assertEqual(even_odd_sort([592, 823, 816, 778, 446, 139, 774, 260, 577, 440, 245, 347, 133, 662, 979, 838, 150, 307, 628, 352, 823, 793, 921, 957, 357, 470, 439, 685, 624, 349]),
                         [150, 979, 260, 352, 440, 957, 446, 470, 921, 592, 823, 823, 793, 624, 685, 628, 662, 577, 774, 778, 439, 357, 349, 347, 307, 816, 245, 139, 838, 133])

    def test_07(self):
        self.assertEqual(even_odd_sort([58, 110, 292, 113, 104, 154, 216, 63, 142, 268, 132, 50, 200, 26, 194, 223, 211, 259, 16, 40, 52, 190, 239, 29, 187, 175, 158, 87, 85, 80, 251, 87, 55, 139, 130, 160, 288, 269, 213, 246, 232, 85, 246, 104, 217, 145, 94, 54, 126, 205, 228, 121, 286, 33, 223, 166, 225, 263, 299, 93]),
                         [16, 26, 40, 299, 50, 52, 54, 269, 58, 80, 94, 104, 104, 110, 126, 263, 259, 251, 130, 132, 142, 154, 239, 225, 223, 223, 158, 217, 213, 160,
                             211, 205, 187, 175, 166, 190, 194, 145, 139, 200, 216, 121, 228, 232, 113, 93, 246, 246, 268, 87, 286, 87, 288, 85, 85, 292, 63, 55, 33, 29])

    def test_08(self):
        self.assertEqual(
            even_odd_sort([21, 71, 98, 52, 52, 97, 64, 18, 58, 8, 6, 34, 52, 92, 63, 6, 97, 18, 16, 37, 27, 62, 55, 1, 2, 50, 36, 16, 5, 24, 46, 67, 90, 9, 29, 89, 30, 41, 76, 53, 41, 3, 31, 75, 87, 45, 43, 63,
                           34, 93, 82, 4, 30, 66, 45, 1, 59, 77, 5, 14, 2, 64, 48, 40, 25, 39, 26, 25, 68, 99, 72, 31, 2, 10, 55, 14, 62, 4, 87, 47, 92, 13, 89, 67, 6, 1, 26, 19, 88, 91, 64, 5, 39, 82, 21, 87, 48, 41, 76, 8]),
            [99, 97, 2, 2, 2, 97, 4, 4, 6, 6, 6, 8, 8, 10, 93, 14, 91, 14, 16, 89, 89, 16, 87, 87, 18, 18, 24, 26, 87, 26, 30, 77, 30, 75, 71, 67, 34, 67, 34, 63, 63, 59, 55, 55, 53, 47, 45, 45, 36, 43, 40, 46, 48, 48, 41, 41, 41, 39, 39, 50, 52, 52, 52, 58, 37, 31, 62, 31, 62, 29, 64, 27, 64, 64, 25, 66, 68, 72, 25, 21, 76, 21, 19, 13, 76, 9, 82, 5, 82, 5, 88, 5, 3, 90, 1, 1, 92, 1, 92, 98])


if __name__ == '__main__':
    unittest.main(verbosity=2)
