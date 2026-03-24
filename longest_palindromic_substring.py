"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def isPalindrom(self, s: str) -> bool:
        if(len(s) == 0):
            return False
        elif(len(s) == 1):
            return True
        elif(len(s) == 2):
            return (s[0] == s[1])
        elif(len(s) == 3):
            return (s[0] == s[2])
        elif(len(s) % 2 == 0):
            return (s[0 : (len(s) // 2)] == s[ : (len(s) // 2 - 1) : -1])
        elif(len(s) % 2 == 1):
            return (s[0 : (len(s) // 2)] == s[ : (len(s) // 2) : -1])

        return False

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        result = ""

        for start in range(len(s)):
            for end in range(len(s), start, -1):
                substr = s[start : end]
                if(self.isPalindrom(substr) and len(substr) > max_length):
                    max_length = len(substr)
                    result = substr
                    break

        return result
        
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        s2 = s[ : : -1]
        max_length = 0
        result = ""

        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substr = s[start : end]
                if(substr in s2):
                    if(substr == substr[ : : -1] and len(substr) > max_length):
                        max_length = len(substr)
                        result = substr
                else:
                    break

        return result

class Solution3:
    def longestPalindrome(self, s: str) -> str:
        hashmap = dict()
        max_length = 0
        result = ""

        for start in range(len(s)):
            if s[start] in hashmap:
                hashmap[s[start]] = hashmap[s[start]] + [start]
            else:
                hashmap[s[start]] = [start]

        for items in hashmap.values():
            for start in range(len(items)):
                for end in range(start, len(items)):
                    substr = s[items[start] : items[end] + 1]
                    if(substr == substr[ : : -1] and len(substr) > max_length):
                        max_length = len(substr)
                        result = substr

        return result
        