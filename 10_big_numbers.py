"""
Given a two-dimensional integer matrix, return the total
number of integers whose value is the largest in its row
and in its column. 

For example, given
1 3 2
4 6 5
1 5 7
Return 2 since 6 and 7 meet the criteria.

Example 1
Input
matrix = [[1, 3, 2],
[6, 6, 5],
[1, 5, 7]]

Output
3

Explanation
The 3 big numbers are 6, 6, and 7.
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

# zip & unpacking - may come in handy


def big_numbers(matrix):
    rows = matrix
    cols = list(zip(*matrix))
    row_maxes = [max(row) for row in rows]
    col_maxes = [max(col) for col in cols]
    a = []
    for r in range(len(rows)):
        for c in range(len(cols)):
            v = rows[r][c]
            if (row_maxes[r], col_maxes[c]) == (v, v):
                a.append(v)
    return len(a)


# DO NOT TOUCH THE BELOW CODE
class TestBigNumbers(unittest.TestCase):

    def test_01(self):
        self.assertEqual(big_numbers([[1, 3, 2], [6, 6, 5], [1, 5, 7]]), 3)

    def test_02(self):
        self.assertEqual(big_numbers([[1, 3, 2], [4, 6, 5], [1, 5, 7]]), 2)

    def test_03(self):
        self.assertEqual(big_numbers([[0]]), 1)

    def test_04(self):
        self.assertEqual(big_numbers([[0, 1, 2, 3, 4]]), 1)

    def test_05(self):
        self.assertEqual(big_numbers([[1, 1, 1, 1, 1]]), 5)

    def test_06(self):
        self.assertEqual(big_numbers([[1],
                                      [1],
                                      [1],
                                      [1],
                                      [1]]), 5)

    def test_07(self):
        self.assertEqual(big_numbers([[0],
                                      [1],
                                      [2],
                                      [3],
                                      [4]]), 1)

    def test_08(self):
        self.assertEqual(big_numbers([[34, 57, 107, 134, 175, 234, 158525, 241, 409, 442, 458, 650, 682, 709, 794, 809, 813, 818, 848, 889],
                                      [80, 188, 197, 218, 255, 290, 437, 529, 529, 535, 653, 666, 779, 815, 819, 904207, 859, 902, 915, 971]]), 2)

    def test_09(self):
        self.assertEqual(big_numbers([[9, 40, 88, 205, 263, 301, 308, 351, 430, 524, 548, 567, 582, 623, 695, 753, 826, 851, 955, 1009, 1013],
                                      [17, 90, 114, 255, 312, 359, 364, 471, 484, 538, 545,
                                          565, 574, 604, 728, 752, 839, 846, 901, 997, 1017],
                                      [117, 159, 174, 208, 257, 293, 310, 371, 420, 426, 543,
                                          583, 588, 642, 765, 781, 829, 830, 935, 940, 985],
                                      [13, 54, 113, 113, 119, 122, 285, 332, 418, 422, 462,
                                       501, 534, 634, 764, 816, 832, 883, 893, 936, 955],
                                      [6, 56, 60, 111, 177, 177, 328, 353, 508, 513, 517,
                                       626, 727, 760, 784, 828, 865, 943, 946, 997, 1001],
                                      [127, 216, 237, 287, 295, 304, 312, 320, 384, 448, 456,
                                       475, 605, 645, 722, 782, 799, 852, 946, 971, 1004],
                                      [139, 232, 243, 342, 374, 414, 428, 434, 435, 498, 681,
                                       692, 712, 759, 763, 821, 826, 889, 922, 956, 1024],
                                      [14, 183, 247, 316, 494, 548, 554, 586, 586, 638, 664,
                                       717, 718, 777, 808, 838, 936, 951, 968, 1017, 1017],
                                      [24, 108, 208, 218, 221, 240, 423, 433, 467, 472, 533,
                                       599, 756, 859, 886, 887, 903, 954, 980, 987, 1002],
                                      [4, 81, 108, 112, 146, 265, 271, 302, 404, 473, 485,
                                       533, 538, 717, 756, 810, 933, 966, 1010, 1017, 1022],
                                      [84, 192, 208, 265, 276, 333, 366, 372, 450, 453, 490,
                                       527, 568, 586, 592, 609, 746, 786, 871, 924, 979],
                                      [14, 42, 85, 276, 331, 368, 412, 457, 555, 641, 693,
                                       715, 745, 757, 868, 933, 937, 959, 983, 1004, 1006],
                                      [232, 315, 360, 384, 396, 424, 433, 481, 534, 545, 634, 701, 874, 875, 899, 951, 960, 963, 972, 997, 998]]), 2)

    def test_10(self):
        self.assertEqual(big_numbers([[6, 4, 3, 8, 1, 6],
                                      [2, 3, 9, 5, 9, 4],
                                      [3, 8, 6, 1, 2, 6],
                                      [3, 9, 2, 1, 7, 5],
                                      [2, 7, 9, 5, 9, 0],
                                      [8, 0, 8, 2, 5, 1]]), 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
