"""
Question: Two Sum
Leetcode - 1: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

"""
Approach 1: 
Initialize a dict to keep track of visited elements and their indices
Traverse the list of numbers, check if the difference i.e. target minus current element exists in the prev visited dict.
if it exists, get it's index, return it along with cuurent index in ascending order.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        prev = {}
        for i in range (0, len(nums)):
            if (target - nums[i]) not in prev:
                prev[nums[i]] = i
            else:
                index_diff = prev.get(target - nums[i])
                if index_diff > i: 
                    return [i, index_diff] 
                else: 
                    return [index_diff, i] 
                

#Driver Code
obj = Solution()
output = obj.twoSum([2,11,15,7], 9)
print(output)