class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = 0
        while left <= right:
            middle = (left + right) // 2
            test_k = middle
            hours = 0
            for i in piles:
                hours += math.ceil(i / test_k)                 
            if hours > h:
                left = middle + 1
            else:
                k = test_k
                right = middle - 1
        return k



            