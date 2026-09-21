## Problem: Valid Anagram (Easy)

**Link:** [Valid Anagram - LeetCode Submission](https://leetcode.com/problems/valid-anagram/submissions/2143429631/)

### Approach
Used a hash map (Python's `Counter`) to count the frequency of each
character in both strings, then compared the two counts directly. Before
counting, I first check whether the strings are the same length — if not,
they can't possibly be anagrams, so we can return early without doing any
counting work.

### Complexity
- Time: O(n) — building each Counter takes O(n), and comparing two Counters
  of size at most 26 (or the alphabet size) is effectively O(1)
- Space: O(1) — since the character set is fixed (lowercase English
  letters), the hash maps have a bounded size regardless of input length

### Notes
The length check up front matters — without it, `Counter("a", "ab")` would
still just compare counts and correctly return False, but it's wasted work
on inputs that can never match. Next time, I'd try the alternative approach
of sorting both strings and comparing them directly (`sorted(s) == sorted(t)`)
— it's more concise but runs in O(n log n) instead of O(n), so it's a
trade-off between readability and efficiency worth knowing about.
