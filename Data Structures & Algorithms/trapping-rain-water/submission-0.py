class Solution:
    def trap(self, height: List[int]) -> int:
        minmax = [0] * len(height)
        for i in range(0, len(height) - 1):
            left = i
            right = i
            left_max = 0
            right_max = 0
            while left >= 0:
                left_max = max(left_max, height[left])
                left -= 1
            while right <= len(height) - 1:
                right_max = max(right_max, height[right])
                right += 1
            minmax[i] = min(left_max, right_max)

        result = 0
        for i in range(len(height) - 1):
            check = minmax[i] - height[i]
            if check > 0:
                result += check
        return result
            



