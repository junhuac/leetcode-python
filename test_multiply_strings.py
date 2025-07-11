"""
https://leetcode.com/problems/multiply-strings/

Medium
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
import unittest
from multiply_strings import Solution

class TestSolution(unittest.TestCase):
    def test_multiply_strings(self):
        solution = Solution()
        self.assertEqual(solution.multiply("2", "3"), "6")

    def test_multiply_medium_strings(self):
        solution = Solution()
        self.assertEqual(solution.multiply("9", "99"), "891")

    def test_multiply_medium_strings_2(self):
        solution = Solution()
        self.assertEqual(solution.multiply("237", "284"), "67308")

    def test_multiply_medium_strings_3(self):
        solution = Solution()
        self.assertEqual(solution.multiply("123", "456"), "56088")

    def test_multiply_medium_strings_4(self):
        solution = Solution()
        self.assertEqual(solution.multiply("52", "60"), "3120")

    def test_multiply_long_strings(self):
        solution = Solution()
        self.assertEqual(solution.multiply("123456789", "987654321"), "121932631112635269")

if __name__ == "__main__":
    unittest.main()