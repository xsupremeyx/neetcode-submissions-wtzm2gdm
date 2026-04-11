class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):
            get = target - nums[i]
            if get in hashMap and hashMap[get] != i:
                return [i,hashMap.get(get)]
        return [-1,-1]
