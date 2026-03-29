class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        for letter in s:
            hashMap1[letter] = hashMap1.get(letter,0) + 1
        
        for letter in t:
            hashMap2[letter] = hashMap2.get(letter,0) + 1

        if(hashMap1 == hashMap2):
            return True
        return False
        