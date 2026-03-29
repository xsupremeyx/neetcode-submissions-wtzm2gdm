class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        solution = 0
        for num in nums:
            solution ^= num
        return solution