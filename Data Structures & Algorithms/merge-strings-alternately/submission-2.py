class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if i == j:
                res.append(word1[i])
                i+=1
            else:
                res.append(word2[j])
                j+=1
        
        res.append(word1[i:])
        res.append(word2[j:])
        
        return "".join(res)
    
# abc xyz
# i 0 1 2 3
# j 0 1 2
# output: axbyc