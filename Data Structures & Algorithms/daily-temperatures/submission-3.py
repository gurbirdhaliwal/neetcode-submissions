class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)] # (val, index)
        i = 1
        while i <= len(temperatures) - 1:
            if stack and temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    val, index = stack.pop()
                    result[index] = i - index
                stack.append((temperatures[i], i))
            i += 1 
        return result
        