"""
Given three integers from 0 to 255 representing the red, green
and blue channels of a color, return the hex string for that color.

The hex string of a color is of the form #RRGGBB, 
where RR is the hexadecimal value of the red channel, and so on.

Example 1
Input
r = 0
g = 0
b = 0

Output
"#000000"

Example 2
Input
r = 255
g = 0
b = 0

Output
"#FF0000"
Explanation

255 is FF in hexadecimal
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def css_trick(r=0, g=0, b=0):
    def value(num):
        if num==0:
            return '00'
        else:
            s=str((hex(num)))
            val=s[2:5]
            val=val.upper()
            return val
    hex_val='#'+value(r)+value(g)+value(b)
    return hex_val


# DO NOT TOUCH THE BELOW CODE
class TestCSSTrick(unittest.TestCase):

    def test_01(self):
        self.assertEqual(css_trick(), '#000000')

    def test_02(self):
        self.assertEqual(css_trick(r=255), '#FF0000')

    def test_03(self):
        self.assertEqual(css_trick(r=255, b=212, g=17), '#FF11D4')

    def test_04(self):
        self.assertEqual(css_trick(b=212, g=17), '#0011D4')

    def test_05(self):
        self.assertEqual(css_trick(b=212, r=17), '#1100D4')

    def test_06(self):
        self.assertEqual(css_trick(b=123, g=231), '#00E77B')

    def test_07(self):
        self.assertEqual(css_trick(r=16, b=16, g=16), '#101010')

    def test_08(self):
        self.assertEqual(
            css_trick(r=63, b=127, g=190), '#3FBE7F')


if __name__ == '__main__':
    unittest.main(verbosity=2)
