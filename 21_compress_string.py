"""
Given a string s, eliminate consecutive duplicate
characters from the string and return it.

Basically, if a list contains repeated character they should be replaced with a single copy of the character. The order of the elements should not be changed.

Example 1
Input
s = "aaaaaabbbccccaaaaddf"

Output
"abcadf"

Example 2
Input
s = "a"

Output
"a"
"""
import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def compress_string(s):
    res = ""
    for i in s:
        if len(res) == 0 or res[-1] != i:
            res += i
    return res

# DO NOT TOUCH THE BELOW CODE
class TestCompressString(unittest.TestCase):

    def test_01(self):
        self.assertEqual(compress_string("aaaaaabbbccccaaaaddf"), "abcadf")

    def test_02(self):
        self.assertEqual(compress_string("a"), "a")

    def test_03(self):
        self.assertEqual(compress_string("gggee"), "ge")

    def test_04(self):
        self.assertEqual(compress_string("iiiio"), "io")

    def test_05(self):
        self.assertEqual(compress_string("eeeeeee"), "e")

    def test_06(self):
        self.assertEqual(compress_string("nnnnddd"), "nd")

    def test_07(self):
        self.assertEqual(compress_string("hhhpddpddd"), "hpdpd")

    def test_08(self):
        self.assertEqual(compress_string("xxbbebbzzzzz"), "xbebz")

    def test_09(self):
        self.assertEqual(compress_string("uuuxxxxxxxxxnn"), "uxn")

    def test_10(self):
        self.assertEqual(compress_string("ffffoffffoooooott"), "fofot")

    def test_11(self):
        self.assertEqual(compress_string(
            "kedegdgsbxdpiojryvgetsdxqzwimayqydxqcdagwnonnnjlngzlbasjplmr"), "kedegdgsbxdpiojryvgetsdxqzwimayqydxqcdagwnonjlngzlbasjplmr")

    def test_12(self):
        self.assertEqual(compress_string(
            "sneuxiyhpmxxzorlqhlavziavitubckpdyswwurbroagictpmkccxkdxtevbvjgzqdeluerdyrowphff"), "sneuxiyhpmxzorlqhlavziavitubckpdyswurbroagictpmkcxkdxtevbvjgzqdeluerdyrowphf")


if __name__ == '__main__':
    unittest.main(verbosity=2)
