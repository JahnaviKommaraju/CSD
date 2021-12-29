"""
Find the largest number in a rotated sorted list
You are given a list of integers nums that is sorted
in ascending order and is rotated at some pivot point.
Find the maximum number in the rotated list.

Example 1
Input
arr = [6, 7, 8, 1, 4]

Output
8

Explanation
The original sorted array of [1, 4, 6, 7, 8] was rotated at index 2 and results in the input array [6, 7, 8, 1, 4,]. And the largest number is 8.

Example 2
Input
arr = [1, 2, 3]

Output
3

Example 3
Input
arr = [1]

Output
1

Example 4
Input
arr = [10, 1, 2, 3, 4, 7]

Output
10
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def largest(arr):
    return max(arr)


# DO NOT TOUCH THE BELOW CODE
class TestLargest(unittest.TestCase):

    def test_01(self):
        self.assertEqual(largest([6, 7, 8, 1, 4]), 8)

    def test_02(self):
        self.assertEqual(largest([1, 2, 3]), 3)

    def test_03(self):
        self.assertEqual(largest([1]), 1)

    def test_04(self):
        self.assertEqual(largest([10, 1, 2, 3, 4, 7]), 10)

    def test_05(self):
        self.assertEqual(
            largest([48, 49, 54, 55, 66, 67, 93, 95, 97, 20, 22, 28, 28, 36, 45]), 97)

    def test_06(self):
        self.assertEqual(largest([84, 85, 93, 97, 99, 100, 11, 14, 14, 15, 19, 26, 28, 31, 31, 38, 40, 46, 55, 56, 58, 58, 59, 59, 63, 68, 68, 68, 72, 82]
                                 ), 100)

    def test_07(self):
        self.assertEqual(largest([251, 281, 301, 302, 326, 328, 345, 356, 363, 364, 373, 373, 385, 395, 398, 409, 419, 424, 428, 430, 434, 437,
                                  446, 456, 484, 499, 15, 36, 49, 49, 71, 81, 89, 97, 98, 99, 113, 143, 150, 161, 185, 190, 204, 205, 207, 210, 225, 231, 245, 249]), 499)

    def test_08(self):
        self.assertEqual(largest([344, 344, 345, 347, 353, 355, 358, 359, 362, 370, 388, 392, 395, 395, 398, 404, 405, 406, 413, 415, 415, 418, 418, 424, 425, 427, 429, 430, 430, 438, 439, 445, 448, 457, 458, 459, 462, 465, 466, 468, 471, 473, 474, 476, 482, 484, 485, 490, 499, 505, 515, 529, 532, 542, 548, 552, 554, 559, 563, 564, 575, 576, 579, 586, 592, 593, 594, 612, 612, 614, 614, 618, 620, 627, 628, 637, 637, 638, 640, 644, 645, 649, 652, 658, 661, 662, 665, 672, 685, 692, 695,
                                  697, 698, 698, 11, 16, 29, 30, 31, 33, 33, 33, 43, 45, 52, 55, 57, 59, 71, 72, 79, 79, 79, 85, 87, 89, 94, 98, 100, 102, 103, 104, 110, 112, 116, 118, 121, 122, 124, 133, 133, 134, 136, 147, 153, 157, 159, 161, 167, 177, 179, 182, 182, 183, 189, 199, 202, 202, 216, 216, 217, 218, 223, 227, 228, 228, 243, 254, 255, 255, 256, 260, 263, 265, 265, 266, 269, 271, 275, 278, 278, 280, 285, 293, 298, 300, 300, 302, 312, 313, 316, 318, 324, 332, 333, 335, 336, 336, 337, 341]), 698)


if __name__ == '__main__':
    unittest.main(verbosity=2)
