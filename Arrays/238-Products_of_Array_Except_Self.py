"""
Question: Products of Array Except Self
Leetcode - 238: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20


"""

"""
Thought 1: Multiply all elements in the array to have a total multiplied value.
Loop through the array and now divide total value by each element.

Fails when array contains 0, as total value becomes zero!
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_multiplied_val = 1
        result_arr = []

        for num in nums:
            total_multiplied_val = total_multiplied_val *num

        print("Debug : total_multuplied_val", total_multiplied_val)
        for i in range(len(nums)):
            print(i)
            result_arr.append(int(total_multiplied_val/nums[i]))
        return result_arr
"""
Looked at solution explaination, did not look at code
Attempt 2: Prefix, Suffix approach
This can be further optimized as per neetcode by not calculating prefix and postfix in separate arrays.
"""
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Calclulating prefix multiplication i.e. all numbers before i
        prefix = [1]
        for i in range(len(nums)):
            if i != 0:
                prefix.append(prefix[i -1] * nums[i -1])

        #Calclulating suffix multiplication i.e. all numbers after i
        suffix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1): # Traversing nums right to left
            if i != (len(nums) -1):
                suffix[i] = suffix[i + 1] * nums[i + 1]

        #print("Debug")
        #print("prefix:",prefix)
        #print("suffix",suffix)
        
        #Calculating final result
        result = []
        for a,b in zip(prefix,suffix):
            result.append(a*b)       

        return result

"""
Optimization attempt 1 without looking at code.
Not using separate arrays for calculating prefix and postfix
"""
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Initializing result array with length equal to nums
        result = [1] * len(nums)

        #Calclulating prefix multiplication i.e. all numbers before i
        #Traversing nums left to right
        for i in range(len(nums)):
            if i == 0: # Handling case for First element as it has nothing to it's left i.e. no prefix 
                result[i] = 1
            else:
                result[i] = result[i - 1] * nums[i - 1]
        
        #Calclulating suffix multiplication i.e. all numbers after i
        #Traversing nums right to left
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) -1): #Handling case for Last element has nothing to it's right i.e. no suffix so final number will just be the existing prefix multiplication
                continue
            else:
                suffix =  suffix * nums[i + 1]
                result[i] = result[i] * suffix # (existing prefix value in result of i cell) x (Calculated suffix value)
        return result


            

#Driver Code
obj = Solution3()
op = obj.productExceptSelf([-1,0,1,2,3])

print("========OUTPUT=========")
print(op)