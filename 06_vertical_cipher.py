"""
Given a string s and an integer n, rearrange s into n rows
so that s can be read vertically (top-down, left to right).

For example, given s = "abcdefghi" and n = 5, return:

["af",
 "bg",
 "ch",
 "di",
 "e"]

Example 1
Input
s = "abcdefghi"
n = 5

Output
["af", "bg", "ch", "di", "e"]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

# Extended Slices may be handy
# https://docs.python.org/release/2.3.5/whatsnew/section-slices.html


def vertical_cipher(s, n):
    return [s[i::n] for i in range(n)]


# DO NOT TOUCH THE BELOW CODE
class TestVerticalCipher(unittest.TestCase):

    def test_01(self):
        self.assertEqual(vertical_cipher("abcdefghi", 5),
                         ["af", "bg", "ch", "di", "e"])

    def test_02(self):
        self.assertEqual(vertical_cipher("abcdefghi", 1), ["abcdefghi"])

    def test_03(self):
        self.assertEqual(vertical_cipher("abcdefghijk", 2),
                         ['acegik', 'bdfhj'])

    def test_04(self):
        self.assertEqual(vertical_cipher(
            "zytRmIzUGUXQRNWtPEtbAFxXjbbyph", 11), ['zQx', 'yRX', 'tNj', 'RWb', 'mtb', 'IPy', 'zEp', 'Uth', 'Gb', 'UA', 'XF'])

    def test_05(self):
        self.assertEqual(vertical_cipher(
            "fvxsyfjlwzgearzhjslsvpsfrzhvvoibtawevxrjajjrdfmjdf", 7), ['flzpvejf', 'vwhsovr', 'xzjfixd', 'sgsrbrf', 'yelztjm', 'fashaaj', 'jrvvwjd'])

    def test_06(self):
        self.assertEqual(vertical_cipher(
            "teXjMVzJuJjiIuqxuvxcprUGNfKmirUJtRHVFyHsprYOSkijHg", 13), ['tuKs',
                                                                        'eqmp',
                                                                        'Xxir',
                                                                        'jurY',
                                                                        'MvUO',
                                                                        'VxJS',
                                                                        'zctk',
                                                                        'JpRi',
                                                                        'urHj',
                                                                        'JUVH',
                                                                        'jGFg',
                                                                        'iNy',
                                                                        'IfH'])

    def test_07(self):
        self.assertEqual(vertical_cipher(
            "EiWWETWETcaZvTbBStqHxiWxqvqSeQGGrMaeOABoaJGCkZbRaZfJwgccIUkCquSewkSFxt", 17), ['EtaJx',
                                                                                            'iqewt',
                                                                                            'WHOg',
                                                                                            'WxAc',
                                                                                            'EiBc',
                                                                                            'TWoI',
                                                                                            'WxaU',
                                                                                            'EqJk',
                                                                                            'TvGC',
                                                                                            'cqCq',
                                                                                            'aSku',
                                                                                            'ZeZS',
                                                                                            'vQbe',
                                                                                            'TGRw',
                                                                                            'bGak',
                                                                                            'BrZS',
                                                                                            'SMfF'])

    def test_08(self):
        self.assertEqual(vertical_cipher(
            "JLjkJ46LXVSPFcXBGiQ1fESrN9Ht5CSfgJnrHDuV8sUJkeijMNRIlksmIRtwzLUM0O6MWOPwIOHOiXI3l5jqct2oyTtgO5NrHbEL", 10), ['JSfS8RzPlt',
                                                                                                                          'LPEfsILw5g',
                                                                                                                          'jFSgUlUIjO',
                                                                                                                          'kcrJJkMOq5',
                                                                                                                          'JXNnks0HcN',
                                                                                                                          '4B9remOOtr',
                                                                                                                          '6GHHiI6i2H',
                                                                                                                          'LitDjRMXob',
                                                                                                                          'XQ5uMtWIyE',
                                                                                                                          'V1CVNwO3TL'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
