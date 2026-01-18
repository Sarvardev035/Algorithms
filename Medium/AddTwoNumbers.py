"""
LeetCode Problem 2: Add Two Numbers
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/

Problem Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach: Elementary Math with Carry
        
        We traverse both linked lists simultaneously, adding corresponding digits
        along with any carry from the previous addition. The key is handling the
        carry properly and continuing until both lists are exhausted and there's
        no remaining carry.
        
        Time Complexity: O(max(m, n)) - where m and n are lengths of l1 and l2
        Space Complexity: O(max(m, n)) - for the result linked list
        
        Args:
            l1: First linked list representing a number
            l2: Second linked list representing a number
            
        Returns:
            Linked list representing the sum
        """
        # Dummy head to simplify edge cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Process both lists and any remaining carry
        while l1 or l2 or carry:
            # Get values from current nodes (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list for easy printing."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result1 = solution.addTwoNumbers(l1, l2)
    print(f"Test 1: [2,4,3] + [5,6,4]")
    print(f"Output: {linked_list_to_list(result1)}")
    print(f"Expected: [7,0,8]\n")
    
    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result2 = solution.addTwoNumbers(l1, l2)
    print(f"Test 2: [0] + [0]")
    print(f"Output: {linked_list_to_list(result2)}")
    print(f"Expected: [0]\n")
    
    # Test case 3: 9999999 + 9999 = 10009998
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result3 = solution.addTwoNumbers(l1, l2)
    print(f"Test 3: [9,9,9,9,9,9,9] + [9,9,9,9]")
    print(f"Output: {linked_list_to_list(result3)}")
    print(f"Expected: [8,9,9,9,0,0,0,1]\n")
