class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = nums[:]
        # prefix
        pref = 1
        for i in range(len(nums)):
            output[i] = pref
            pref *= nums[i]
        # postfix
        post = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= post
            post *= nums[i]
        return output
