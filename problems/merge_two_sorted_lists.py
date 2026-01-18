"""Merge two sorted linked lists by splicing nodes together.

Provides a simple ListNode class and helper converters for testing.
"""
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_listnode(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    cur = head
    for v in items[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def listnode_to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    tail = dummy
    a, b = l1, l2
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


if __name__ == "__main__":
    a = list_to_listnode([1, 2, 4])
    b = list_to_listnode([1, 3, 4])
    merged = merge_two_lists(a, b)
    print(listnode_to_list(merged))  # [1,1,2,3,4,4]
