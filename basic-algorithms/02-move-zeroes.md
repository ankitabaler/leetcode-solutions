## Problem: Move Zeroes (Easy)

**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
Used the two-pointer technique: `lastNonZeroFoundAt` tracks the position
where the next non-zero element should go, while `i` scans through the
array. Whenever a non-zero element is found at `i`, it's swapped with the
element at `lastNonZeroFoundAt` using `std::swap`, and that pointer
advances. Since we only swap (never overwrite), zeroes naturally get
pushed to the end while non-zero elements keep their original relative
order.

### Complexity
- Time: O(n) — a single pass through the array
- Space: O(1) — done in-place using only one extra pointer variable

### Notes
Swapping instead of directly assigning is what makes this a one-pass
solution — a naive approach that just overwrites `nums[lastNonZeroFoundAt]`
would need a second pass afterward to fill the remaining slots with zeroes.
Next time, I'd compare this against a "count zeroes then fill" two-pass
approach to see which reads more clearly, even though both are O(n).