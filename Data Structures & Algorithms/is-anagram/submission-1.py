class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_1 = dict()
        d_2 = dict()
        for i in s:
            d_1[i] = d_1.get(i, 0) + 1
        for i in t:
            d_2[i] = d_2.get(i, 0) + 1
        if len(d_1) != len(d_2):
            return False
        for val in d_1:
            if d_1.get(val) == d_2.get(val):
                continue
            else:
                return False
        return True
        
        