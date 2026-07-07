class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0
        for i in nums:
            temp = 1
            curr = i
            while (curr - 1) in s:
                temp += 1
                curr -= 1
            result = max(result, temp)
        return result
        
