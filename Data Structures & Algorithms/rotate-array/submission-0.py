class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # M1
        # temp = nums[:]
        # for i in range(0,len(nums)):
        #     print(f"i: {i}, i+k % len: {(i+k) % len(nums)}")
        #     nums[i] = temp[(i+k) % len(nums)]
        if not nums:
            return
        k = k % len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l + 1
            r = r - 1
        
        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l + 1
            r = r - 1

        l = k
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l = l + 1
            r = r - 1
        
        