class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        aux_stack = []
        for symbol in s:
            if symbol == '(':
                aux_stack.append(symbol)
            elif symbol == ')':
                aux_stack.pop()
            max_depth = max(max_depth, len(aux_stack))
            #print(max_depth)

        return max_depth