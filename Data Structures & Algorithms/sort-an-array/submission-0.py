class Solution:
    def merge(self,left,right):
        numsSort = []
        i = 0
        j = 0
        while (i < len(left)) and (j < len(right)):
            if(left[i]<=right[j]):
                numsSort.append(left[i])
                i+=1
            else:
                numsSort.append(right[j])
                j+=1
        
        while i < len(left):
            numsSort.append(left[i])
            i+=1
        
        while j < len(right):
            numsSort.append(right[j])
            j+=1
        return numsSort
    
    def mergeSort(self,nums,s,e):
        if s == e:
            return [nums[s]]
        else:
            mid = (s+e)//2
            left = self.mergeSort(nums,s,mid)
            right = self.mergeSort(nums,mid+1,e)
            return self.merge(left,right)

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        return self.mergeSort(nums,0,len(nums)-1)
        