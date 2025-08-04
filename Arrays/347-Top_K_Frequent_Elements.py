"""
Question : Top K Frequent Elements
Leetcode - 347: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Create a count map of unique elements
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        #Alternatively count = Counter(nums) also achieves the same thing

        """ Learning element! Syntax and how to sort a dict on values"""
        #Sort the freq counts in descending order
        count = sorted(count.items(), key=lambda item: item[1], reverse=True)

        #Prepare the answer list i.e. K elements from the sorted count
        kfreq = []

        for i in range(k):
            kfreq.append(count[i][0])

        return kfreq

"""
Alternate Approach: Can also use min_heap, build a min heap of size k 
"""
#Driver Code
obj = Solution()
print(obj.topKFrequent([1,2,2,3,3,3],2))
print(obj.topKFrequent([1,1,1,2,2,3],2))

