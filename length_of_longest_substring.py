"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        end = 0

        while start < len(s):
            end = start + 1
            while end < len(s) and s[end] not in s[start : end]:
                end = end + 1
            if(end - start > max_len):
                max_len = end - start
            start += 1

        return max_len

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        end = 0

        while start < len(s):
            map = dict()
            map[s[start]] = start
            end = start + 1
            while end < len(s) and s[end] not in map:
                map[s[end]] = end
                end = end + 1
            if(end - start > max_len):
                max_len = end - start
            if (end < len(s) and s[end] in map):
                start = map[s[end]] + 1
            else:
                start = start + 1

        return max_len

                