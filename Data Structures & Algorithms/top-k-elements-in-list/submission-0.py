class Solution:
    ''' old solutin o(n+m^2) worst
    hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        solution = []
        to_remove = len(hashMap) - k
        while(to_remove > 0):
            minKey = min(hashMap,key=hashMap.get)
            del hashMap[minKey]
            to_remove -= 1
        return list(hashMap.keys())
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        n = len(nums)

        buckets = [None] * (n + 1)

        for i in range(0,n+1):
            buckets[i] = []
        
        for (key,freq) in hashMap.items():
            buckets[freq].append(key)

        solution = []

        for freq in range(n, 0, -1):
            for key in buckets[freq]:
                solution.append(key)
                if len(solution) == k:
                    return solution

        