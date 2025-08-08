"""
Question: Valid Palindrome
Leetcode - 125: https://leetcode.com/problems/valid-palindrome/description/ 

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #String Cleanup as we're considering only alphanumeric characters, this includes removing whitespaces
        s = re.sub("[^a-zA-Z0-9]","",s)
        
        #String to lowercase for comparison
        s = s.lower()

        L, R = 0, len(s) -1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True