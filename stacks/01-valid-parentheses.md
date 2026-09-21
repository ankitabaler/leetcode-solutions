"""
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Task:
Given a string s containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid. A string is valid if:
1. Open brackets are closed by the same type of bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop the top element if stack is not empty, else use a dummy character
                top_element = stack.pop() if stack else '#'

                # If the bracket doesn't match the stack's top element, return False
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)

        # If stack is empty, all opening brackets were matched
        return not stack


# ---------------------------------------------------------------------------
# Local test cases (run this file directly: `python 01-valid-parentheses.py`)
# Test locally BEFORE submitting to LeetCode's judge.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: typical case - simple valid pair
    assert sol.isValid("()") is True, "Test 1 failed"
    print("Test 1 passed: '()' -> True")

    # Test case 2: typical case - mixed valid brackets
    assert sol.isValid("()[]{}") is True, "Test 2 failed"
    print("Test 2 passed: '()[]{}' -> True")

    # Test case 3: typical case - invalid order
    assert sol.isValid("(]") is False, "Test 3 failed"
    print("Test 3 passed: '(]' -> False")

    # Test case 4: edge case - empty string
    assert sol.isValid("") is True, "Test 4 failed"
    print("Test 4 passed: '' -> True")

    # Test case 5: edge case - closing bracket with nothing open
    assert sol.isValid(")") is False, "Test 5 failed"
    print("Test 5 passed: ')' -> False")

    # Test case 6: edge case - nested brackets, correctly matched
    assert sol.isValid("{[]}") is True, "Test 6 failed"
    print("Test 6 passed: '{[]}' -> True")

    # Test case 7: edge case - unclosed opening bracket
    assert sol.isValid("(()") is False, "Test 7 failed"
    print("Test 7 passed: '(()' -> False")

    print("\nAll test cases passed!")