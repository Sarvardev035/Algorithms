"""
LeetCode Problem 9: Palindrome Number
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/

Problem Description:
Given an integer x, return true if x is a palindrome, and false otherwise.

An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Approach: Mathematical reversal (without converting to string)
        
        We reverse the second half of the number and compare it with the first half.
        Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes.
        
        Time Complexity: O(log n) - We process half of the digits
        Space Complexity: O(1) - Only using a few variables
        
        Args:
            x: Integer to check
            
        Returns:
            True if x is a palindrome, False otherwise
        """
        # Negative numbers are not palindromes
        # Numbers ending with 0 are not palindromes (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10 (ignore middle digit)
        return x == reversed_half or x == reversed_half // 10


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    x1 = 121
    result1 = solution.isPalindrome(x1)
    print(f"Test 1: x={x1}")
    print(f"Output: {result1}")
    print(f"Expected: True\n")
    
    # Test case 2
    x2 = -121
    result2 = solution.isPalindrome(x2)
    print(f"Test 2: x={x2}")
    print(f"Output: {result2}")
    print(f"Expected: False\n")
    
    # Test case 3
    x3 = 10
    result3 = solution.isPalindrome(x3)
    print(f"Test 3: x={x3}")
    print(f"Output: {result3}")
    print(f"Expected: False\n")
    
    # Test case 4
    x4 = 12321
    result4 = solution.isPalindrome(x4)
    print(f"Test 4: x={x4}")
    print(f"Output: {result4}")
    print(f"Expected: True\n")
