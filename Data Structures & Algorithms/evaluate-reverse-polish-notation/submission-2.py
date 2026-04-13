import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        aux_stack = []

        for token in tokens:
            if token =='+':
                temp = aux_stack.pop() + aux_stack.pop()
                aux_stack.append(temp)
            elif token =='*':
                temp = aux_stack.pop() * aux_stack.pop()
                aux_stack.append(temp)
            elif token =='-':
                temp = aux_stack.pop(len(aux_stack) - 2) - aux_stack.pop(len(aux_stack) - 1)
                aux_stack.append(temp)
            elif token =='/':
                temp = int(aux_stack.pop(len(aux_stack) - 2) / aux_stack.pop(len(aux_stack) - 1))
                aux_stack.append(temp)
            else:
                aux_stack.append(int(token))
            print(aux_stack)

        return aux_stack[-1]