class Solution:
    def calPoints(self, operations: List[str]) -> int:
        aux_stack = []

        for operation in operations:
            if operation == 'D':
                aux_stack.append(aux_stack[-1] * 2)
            elif operation == '+':
                aux_stack.append(aux_stack[-1] + aux_stack[-2])
            elif operation == 'C':
                aux_stack.pop()
            else:
                aux_stack.append(int(operation))
        
            print(aux_stack)


        return sum(aux_stack)