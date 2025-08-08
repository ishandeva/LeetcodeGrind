"""
Question: Longest Consecutive Sequence
Leetcode -128: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List,Counter

"""
Approach 1: Intuitive Approach
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Handling Edge Case
        if len(nums) == 0:
            return 0
        else:
            #Sort nums, then remove duplicates from sorted nums, then cast into a list
            processedNums = list(Counter(sorted(nums)).keys())
            
            #List to store count values in case of count resets
            #Initialze list with 1 in case there is no need to store anything in it.
            counterList = [1]
            count = 1 #Initialize count with 1 and not zero, as the default consequitive list size would be 1 
            for i in range(len(processedNums)):
                if i == 0:
                    continue
                if abs(processedNums[i] - processedNums[i - 1]) == 1:
                    count += 1
                else:
                    counterList.append(count)
                    count = 1 #If the chain breaks, reset counter
            
            return max(count,max(counterList))

#Driver Code
obj = Solution()
print(obj.longestConsecutive([100,4,200,1,3,2]))
print(obj.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))