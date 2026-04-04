class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    return False
                if top == '(' and c == ')':
                    continue
                elif top == '[' and c == ']':
                    continue
                elif top == '{' and c == '}':
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        return False