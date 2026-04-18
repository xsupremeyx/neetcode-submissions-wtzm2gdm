class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # let even = 0
        # let odd = 2
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] %2 == 0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid] %2 == 1:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
            else:
                mid+=1
        return nums