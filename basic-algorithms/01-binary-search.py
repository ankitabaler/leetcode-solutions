"""
Problem: Binary Search
LeetCode: https://leetcode.com/problems/binary-search/
Difficulty: Easy

Task:
Given a sorted array of distinct integers `nums` and a target value,
return the index of target if it exists, otherwise return -1.
Must run in O(log n) time.
"""


def search(nums: list[int], target: int) -> int:
    """
    Standard iterative binary search on a sorted array.

    Args:
        nums: sorted list of distinct integers
        target: value to search for

    Returns:
        Index of target if found, else -1
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---------------------------------------------------------------------------
# Local test cases (run this file directly: `python 01-binary-search.py`)
# Test locally BEFORE submitting to LeetCode's judge.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Test case 1: typical case - target present in the middle
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4, "Test 1 failed"
    print("Test 1 passed: target found at correct index")

    # Test case 2: typical case - target not present
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1, "Test 2 failed"
    print("Test 2 passed: target correctly reported as absent")

    # Test case 3: edge case - empty array
    assert search([], 5) == -1, "Test 3 failed"
    print("Test 3 passed: empty array returns -1")

    # Test case 4: edge case - single element (match and no match)
    assert search([5], 5) == 0, "Test 4a failed"
    assert search([5], 3) == -1, "Test 4b failed"
    print("Test 4 passed: single-element array handled correctly")

    # Test case 5: edge case - target at the boundaries
    assert search([1, 2, 3, 4, 5], 1) == 0, "Test 5a failed"
    assert search([1, 2, 3, 4, 5], 5) == 4, "Test 5b failed"
    print("Test 5 passed: boundary elements found correctly")

    print("\nAll test cases passed!")