class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in tokens:
            if i in ("+", "-", "/", "*"):
                if len(stack) >= 2:
                    val2 = stack.pop() 
                    val1 = stack.pop()
                    if i == "+":
                        result = val1 + val2
                    elif i == "-":
                        result = val1 - val2
                    elif i == "*":
                        result = val1 * val2
                    else:
                        result = int(val1 / val2)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]


