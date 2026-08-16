class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                if nums[left] <= target and target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            if nums[middle] == target:
                return middle
        return -1
