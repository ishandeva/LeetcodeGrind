"""
Question : Valid Anagram
Leetcode - 242: https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""

"""
Approach 1 : Hashmap
Create a map of the counts of all letters in both strings.
Then compare the maps, if equal (not considering order) return True, else return False.
"""
from typing import Counter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter (t)

        if c1 == c2:
            return True
        else: return False

"""
Approach 2 : Optimized
First check the len of strings, if not equal break & return.
Hardcode string of all letters, and loop through it.
    Count the letter in both strings, if not equal, return False.
    Else, it's an Anagram.
"""
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if s.count(letter) !=  t.count(letter):
                return False
        return True