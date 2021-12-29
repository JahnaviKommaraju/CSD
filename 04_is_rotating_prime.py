import unittest

question_04 = """
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.
"""


# Implement the below function and run the program

def is_rotating_prime(num):
    i = rem = val = total = 0
    n = str(num)
    digits = len(n)
    while i < digits:
        rem = num % 10
        num = num // 10
        num = rem * (10 ** (digits - 1)) + num
        print(num)
        val = is_prime(num)
        total += val
        i += 1
    if total == digits:
        return True
    return False

def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0


class TestIsRotatingPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(2), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(19), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(791), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(919), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
