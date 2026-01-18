"""
LeetCode Problem 1: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Problem Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

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
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Hash Map (One-pass)
        
        We use a hash map to store the numbers we've seen so far along with 
        their indices. For each number, we check if (target - current_number) 
        exists in the hash map.
        
        Time Complexity: O(n) - We traverse the list once
        Space Complexity: O(n) - Hash map stores at most n elements
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing indices of the two numbers that sum to target
        """
        # Dictionary to store number -> index mapping
        seen = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in our map, we found the pair
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # No solution found (shouldn't happen based on problem constraints)
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Output: {result1}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 2]\n")
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Output: {result3}")
    print(f"Expected: [0, 1]\n")
