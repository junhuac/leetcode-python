"""
7. Reverse Integer
Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2**31 <= x <= 2**31 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        digits = []
        number = x
        sign = 1
        if(x < 0):
            sign = -1
            number = -x

        while number > 0:
            digit = number % 10
            digits.append(digit)
            number -= digit
            number //= 10

        result = 0
        for i in digits:
            if(result <= MAX_INT / 10) :
                result *= 10
            else:
                return 0

            if(result <= MAX_INT - i) :
                result += i
            else:
                return 0

        return sign * result
        