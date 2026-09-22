Here is the updated markdown template for the optimized Hash Table approach:

## Problem: Two Sum (Easy)

**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/?utm_source=gemini)

### Approach

Used a Hash Table to map each number's value to its index in a single pass. For each element `nums[i]`, we check if its complement (`target - nums[i]`) already exists in the map. If it exists, we return the pair of indices immediately; otherwise, we store the current number and its index in the Hash Table.

### Complexity

* **Time:** $O(n)$ — Single traversal through the array with average $O(1)$ Hash Table lookups.
* **Space:** $O(n)$ — Memory used to store up to $n$ elements in the Hash Table.

### Notes

* **C++ (`std::unordered_map`):** Provides $O(1)$ average-time insertion and search out of the box.
* **C:** Requires a custom Hash Table implementation using array-based bucket chaining with `malloc` and `free` to prevent memory leaks.
