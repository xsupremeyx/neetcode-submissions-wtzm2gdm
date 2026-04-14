class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        a = sorted(nums)
        for i in range(0, n-1):
            if(i > 0 and a[i] == a[i-1]):
                continue
            left = i+1
            right = n-1
            target = -a[i]
            while ( left < right):
                twoSum = a[left] + a[right]
                if twoSum == target:
                    result.append((a[i],a[left],a[right]))
                    left +=1
                    right -=1
                    while(left < n and a[left] == a[left-1]):
                        left +=1
                    while(right >= 0 and a[right] == a[right+1]):
                        right -=1
                elif twoSum < target:
                    left+=1
                else:
                    right-=1
        return result
