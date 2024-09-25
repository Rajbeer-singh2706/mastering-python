
### 5. **Find All Anagrams in a String**
"""
- **Problem**: Given a string `s` and a string `p`, return the start indices of all the anagrams of `p` in `s`.

Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
"""

s = "cbaebabacd"
p = "abc"

index = []
for idx in range(len(s)):
    c = s[idx]
    if c in p:
        substr=s[idx:idx+3]
        substr =''.join(sorted(substr))
        print(f"sunbstr: {substr}")
        if substr == p:
            index.append(idx)
print(index)