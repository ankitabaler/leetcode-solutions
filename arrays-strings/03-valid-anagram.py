def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True

# --- LOCAL TEST CASES ---
if __name__ == "__main__":
    # Test 1: Typical Case
    print("Test 1 (Typical):", "PASS" if isAnagram("anagram", "nagaram") == True else "FAIL")

    # Test 2: Edge Case (Different lengths)
    print("Test 2 (Edge Case):", "PASS" if isAnagram("rat", "car") == False else "FAIL")