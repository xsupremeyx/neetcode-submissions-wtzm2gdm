class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        outputStr = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if i == j:
                outputStr += word1[i]
                i+=1
            else:
                outputStr += word2[j]
                j+=1
        
        while i < len(word1):
            outputStr += word1[i]
            i+=1
        
        while j < len(word2):
            outputStr += word2[j]
            j+=1
        
        return outputStr
    
# abc xyz
# i 0 1 2 3
# j 0 1 2
# output: axbyc