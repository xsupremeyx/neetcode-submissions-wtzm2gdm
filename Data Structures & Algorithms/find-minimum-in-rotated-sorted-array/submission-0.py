class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        l = 0
        r = len(nums)-1
        while l<=r:
            if l==r:
                return nums[l]
            mid = r + (l-r)//2
            if nums[mid] >= nums[r]:
                l = mid + 1
                continue 
            else:
                r = mid
                continue
        return None