"""
Question: Encode and Decode Strings
Leetcode - 271: https://leetcode.com/problems/encode-and-decode-strings/ (Paid, locked)
Neetcode: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = []
        for string in strs:
            chars = list(string)
            for ch in chars:
                encodedStr.append(ord(ch))
                encodedStr.append('-')
            encodedStr.append(',')
        return ''.join(str(x) for x in encodedStr)
    
    def decode(self, s: str) -> List[str]:
        decodedList = []

        #Splitting commas to get individual words
        words = s.split(",")
        words.pop()
        #Splitting dashes to get individual chars in words
        for word in words:
            chars = word.split("-")
            chars.pop()
            decodedChars = [chr(int(x)) for x in chars]
            decodedList.append("".join(decodedChars))
        return decodedList

#Driver Code
obj = Solution()
op = obj.encode(["yo","yo","ishan","dada"])
op2 = obj.decode(op)

print("=============OUTPUT=============")
print("Encoded String : ", op)
print("Decoded String : ", op2)