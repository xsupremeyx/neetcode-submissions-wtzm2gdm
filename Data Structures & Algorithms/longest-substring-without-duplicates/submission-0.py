class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length = 1
        chars = {}
        l,r = 0,0
        while (r < len(s)):
            if chars.get(s[r],0) >= 1:
                chars[s[l]] = chars[s[l]] - 1
                l+=1
            else:
                length = max(length, r - l + 1)
                chars[s[r]] = 1
                r+=1
        return length