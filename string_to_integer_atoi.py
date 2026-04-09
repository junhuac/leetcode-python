"""
8. String to Integer (atoi)
Medium
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31-1
        MIN_INT = -(2**31)
        sign = None
        digit = None
        result = 0

        for c in s:
            if c == ' ' and digit == None and sign == None:
                continue
            elif c == '+' and digit == None and sign == None:
                sign = 1
                continue
            elif c == '-' and digit == None and sign == None:
                sign = -1
                continue
            elif c == '.':
                break
            elif c == '0':
                digit = 0
            elif c == '1':
                digit = 1
            elif c == '2':
                digit = 2
            elif c == '3':
                digit = 3
            elif c == '4':
                digit = 4
            elif c == '5':
                digit = 5
            elif c == '6':
                digit = 6
            elif c == '7':
                digit = 7
            elif c == '8':
                digit = 8
            elif c == '9':
                digit = 9
            else:
                break

            if(not digit == None):
                if(not result == 0):
                    result *= 10
                result += digit

        if(sign == -1):
            result = -result
        
        if(result > MAX_INT):
            return MAX_INT
        
        if(result < MIN_INT):
            return MIN_INT

        return result
