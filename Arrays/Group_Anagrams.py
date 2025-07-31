"""
Question: Group Anagrams
Leetcode - 49: https://leetcode.com/problems/group-anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


"""
Approach 1: [Failed] Create a hash based on sum of string's chars
Group all strings with same hash value.

Point of failure, different letters can also have the same ord summation!
"""
from typing import List

class Solution:
    def strHash (string: str) -> int:
        sum = 0
        for i in sorted(string):
            sum += ord(i)
        return sum
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            hashvalue = Solution.strHash(string)  
            if hashvalue not in map:
                map[hashvalue] = [string]
            else:
                map[hashvalue].append(string)
        return list(map.values())

"""
Failed Case
I/P: ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]

Expected:
[["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],["bar"],["pew"],["cab"]]

Output: duh and ill are grouped when they should have been separate!
[['max'],['buy'],['doc'],['may'],['duh', 'ill'],['tin'],['bar'],['pew'],['cab']]
"""

"""
Approach 2:
Better Hashing func: Tuples of ord values
"""
class Solution2:
    def strHash (string: str) -> int:
        char_count_arr = [0] * 26
        for ch in string:
            char_count_arr[ord(ch) - ord('a')] += 1
        return tuple(char_count_arr)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            hashvalue = Solution2.strHash(string)
            if hashvalue not in map:
                map[hashvalue] = [string]
            else:
                map[hashvalue].append(string)
        return list(map.values())


#Driver Code
obj = Solution2()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(obj.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
