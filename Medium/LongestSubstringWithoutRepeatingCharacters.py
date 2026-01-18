"""
LeetCode Problem 3: Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: Sliding Window with Hash Map
        
        We use a sliding window approach with two pointers (left and right).
        We expand the window by moving right pointer and keep track of characters
        in a hash map. When we encounter a duplicate, we shrink the window from
        the left until there are no duplicates.
        
        Time Complexity: O(n) - Each character is visited at most twice
        Space Complexity: O(min(m, n)) - where m is charset size
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        # Dictionary to store character and its index
        char_index = {}
        max_length = 0
        left = 0
        
        # Expand window with right pointer
        for right, char in enumerate(s):
            # If character is in window and its index is >= left
            if char in char_index and char_index[char] >= left:
                # Move left pointer to the right of the duplicate
                left = char_index[char] + 1
            
            # Update character's latest index
            char_index[char] = right
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(s1)
    print(f"Test 1: s='{s1}'")
    print(f"Output: {result1}")
    print(f"Expected: 3\n")
    
    # Test case 2
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    print(f"Test 2: s='{s2}'")
    print(f"Output: {result2}")
    print(f"Expected: 1\n")
    
    # Test case 3
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    print(f"Test 3: s='{s3}'")
    print(f"Output: {result3}")
    print(f"Expected: 3\n")
    
    # Test case 4
    s4 = ""
    result4 = solution.lengthOfLongestSubstring(s4)
    print(f"Test 4: s='{s4}'")
    print(f"Output: {result4}")
    print(f"Expected: 0\n")
    
    # Test case 5
    s5 = "dvdf"
    result5 = solution.lengthOfLongestSubstring(s5)
    print(f"Test 5: s='{s5}'")
    print(f"Output: {result5}")
    print(f"Expected: 3\n")
