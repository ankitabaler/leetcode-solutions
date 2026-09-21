"""
Problem: Reverse Linked List
LeetCode: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy

Task:
Given the head of a singly linked list, reverse the list and return
the new head.
"""

from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward

        return prev  # prev becomes the new head


# ---------------------------------------------------------------------------
# Local test cases (run this file directly: `python 01-reverse-linked-list.py`)
# Test locally BEFORE submitting to LeetCode's judge.
# ---------------------------------------------------------------------------
def build_list(vals):
    """Builds a linked list from a Python list and returns its head."""
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def list_to_vals(head):
    """Converts a linked list back into a Python list for easy comparison."""
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: typical case - multiple elements
    test1 = build_list([1, 2, 3, 4, 5])
    result1 = list_to_vals(sol.reverseList(test1))
    assert result1 == [5, 4, 3, 2, 1], f"Test 1 failed: {result1}"
    print("Test 1 passed:", result1)

    # Test case 2: edge case - empty list
    test2 = build_list([])
    result2 = list_to_vals(sol.reverseList(test2))
    assert result2 == [], f"Test 2 failed: {result2}"
    print("Test 2 passed:", result2)

    # Test case 3: edge case - single element
    test3 = build_list([7])
    result3 = list_to_vals(sol.reverseList(test3))
    assert result3 == [7], f"Test 3 failed: {result3}"
    print("Test 3 passed:", result3)

    # Test case 4: edge case - two elements
    test4 = build_list([1, 2])
    result4 = list_to_vals(sol.reverseList(test4))
    assert result4 == [2, 1], f"Test 4 failed: {result4}"
    print("Test 4 passed:", result4)

    print("\nAll test cases passed!")