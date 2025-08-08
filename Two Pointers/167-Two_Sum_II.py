"""
Question: Two Sum II - Input Array is Sorted
Leetcode -167: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

from typing import List

"""
Two pointers at the two ends of the array.
Since the array is already sorted in ascending order, L pointer is the smallest number and vice versa for R

We check the sum of L & R, if it's more than target, then we can say for sure that the number at R, will not be a part of the answer.
    Why? Cause it's the largest of the list and if by adding the smallest to it (i.e. L) sum is still more than target, 
    then that means that the Largest  i.e. R will not add to the target, no matter what other numbers we add to it.

    So in this case we skip R and decrease the pointer to the second largest.. and so on.

We check if the sum of L & R is less than target, in that case the number at L, will not be a part of the answer.
    FOllows the same logic as above i.e. L will not add to the target no matter what other numbers we add to it.

If both the above conditions are false, that means sum is equal to target, return answer.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L + 1, R + 1] 