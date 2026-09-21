#include <iostream>
#include <vector>

/*
Problem: Move Zeroes
LeetCode: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy

Task:
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements. Must be done
in-place without making a copy of the array.
*/

class Solution {
public:
    void moveZeroes(std::vector<int>& nums) {
        int lastNonZeroFoundAt = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                std::swap(nums[lastNonZeroFoundAt++], nums[i]);
            }
        }
    }
};

// ---------------------------------------------------------------------------
// Local test cases (compile & run: g++ 02-move-zeroes.cpp -o test && ./test)
// Test locally BEFORE submitting to LeetCode's judge.
// ---------------------------------------------------------------------------
void printVec(const std::vector<int>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v[i];
        if (i != v.size() - 1) std::cout << ", ";
    }
    std::cout << "]";
}

int main() {
    Solution sol;

    // Test case 1: typical case - zeroes scattered throughout
    std::vector<int> test1 = {0, 1, 0, 3, 12};
    sol.moveZeroes(test1);
    std::cout << "Test 1: ";
    printVec(test1);
    std::cout << (test1 == std::vector<int>{1, 3, 12, 0, 0} ? " -> PASS" : " -> FAIL") << std::endl;

    // Test case 2: edge case - no zeroes at all
    std::vector<int> test2 = {1, 2, 3};
    sol.moveZeroes(test2);
    std::cout << "Test 2: ";
    printVec(test2);
    std::cout << (test2 == std::vector<int>{1, 2, 3} ? " -> PASS" : " -> FAIL") << std::endl;

    // Test case 3: edge case - empty array
    std::vector<int> test3 = {};
    sol.moveZeroes(test3);
    std::cout << "Test 3: ";
    printVec(test3);
    std::cout << (test3 == std::vector<int>{} ? " -> PASS" : " -> FAIL") << std::endl;

    // Test case 4: edge case - all zeroes
    std::vector<int> test4 = {0, 0, 0};
    sol.moveZeroes(test4);
    std::cout << "Test 4: ";
    printVec(test4);
    std::cout << (test4 == std::vector<int>{0, 0, 0} ? " -> PASS" : " -> FAIL") << std::endl;

    // Test case 5: edge case - single element
    std::vector<int> test5 = {0};
    sol.moveZeroes(test5);
    std::cout << "Test 5: ";
    printVec(test5);
    std::cout << (test5 == std::vector<int>{0} ? " -> PASS" : " -> FAIL") << std::endl;

    std::cout << "\nAll test cases executed!" << std::endl;
    return 0;
}