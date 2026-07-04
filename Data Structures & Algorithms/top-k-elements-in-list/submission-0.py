class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        s = dict()
        for i in nums:
            s[i] = s.get(i, 0) + 1

        for count in range (k):
            largest_key = None
            largest_val = None
            for key, val in s.items():
                if (largest_key is None) or (val > largest_val):
                    largest_key = key
                    largest_val = val
            s.pop(largest_key)
            result.append(largest_key)
        return result
                
