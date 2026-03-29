class Solution:
    def binSrch(self,arr,target,s,e):
        if(s>=e):
            if(s>=len(arr)):
                return -1
            if((target == arr[s])):
                return s
            return -1
        
        mid = int((s+e)/2)
        if(target == arr[mid]):
            return mid
        elif(target < arr[mid]):
            return self.binSrch(arr,target,s,mid-1)
        else:
            return self.binSrch(arr,target,mid+1,e)

    def search(self, nums: List[int], target: int) -> int:
        return self.binSrch(nums,target,0,len(nums)-1)