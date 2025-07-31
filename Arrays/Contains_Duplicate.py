"""
Question: Contains Duplicate
Leetcode - 217: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
Approach 1 : Using Dict/Hashmap
Create a count map for every element in the array.
If the count exceeds 1 (i.e. that element occured twice), return True.
"""
from typing import List

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
                return True
            else:
                count[i] = 1
        return False

"""
Approach 2 : Using a Set/List
Maintain a "seen" set or list.
Traverse the array, if element not in "seen", add it to "seen", else return True. (i.e. element exists in seen i.e. it has occured twice)
"""

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False