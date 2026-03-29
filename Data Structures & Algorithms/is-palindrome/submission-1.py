class Solution:
    def validPalindrome(self, s):
        end = len(s) - 1
        mid = len(s)/2
        for i in range(0,int(mid)):
            if(s[i] != s[end-i]):
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        sf = ''.join(ch for ch in s.lower() if ch.isalnum())
        return self.validPalindrome(sf)
        