class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if stack:
                    val = stack.pop() + i
                    if val == "()" or val == "{}" or val == "[]":
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
            
        return True