class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        puts = 1
        moves = 1
        while moves < len(nums):
            if(nums[moves] != nums[moves-1]):
                nums[puts] = nums[moves]
                puts+=1
                moves+=1
                continue
            moves+=1
        return puts