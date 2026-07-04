class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        d2 = {i: [] for i in range(1, len(nums) + 1)}
        for i in nums:
            d1[i] = d1.get(i, 0) + 1
        for key, val in d1.items():
            d2[val].append(key)
        result = []
        for i in range(len(nums), 0, -1):
            while d2[i]:
                val = d2[i].pop()
                result.append(val)
                if len(result) == k:
                    return result

            
