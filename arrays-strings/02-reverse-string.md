## Problem: Reverse String (Easy)
**Link:** [https://leetcode.com/problems/reverse-string/](https://leetcode.com/problems/reverse-string/?utm_source=gemini)



### Code
```c
void reverseString(char* s, int sSize) {
    int left = 0;
    int right = sSize - 1;

    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
}
