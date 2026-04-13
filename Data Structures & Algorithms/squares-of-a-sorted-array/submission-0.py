class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        if len(neg) == 0:
            return [x*x for x in nums]
        
        elif len(pos) == 0:
            return [x*x for x in nums][::-1]
        
        else:
            neg = [x*x for x in neg][::-1]
            pos = [x*x for x in pos]

        ans = []
        i = 0
        j = 0

        while( i < len(neg) and j < len(pos)):
            if neg[i]<pos[j]:
                ans.append(neg[i])
                i+=1
            else:
                ans.append(pos[j])
                j+=1
        while( i < len(neg)):
            ans.append(neg[i])
            i+=1
            
        while( j < len(pos)):
            ans.append(pos[j])
            j+=1
            
        return ans

