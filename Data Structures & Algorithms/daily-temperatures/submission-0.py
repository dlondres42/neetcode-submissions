class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        aux_stack = [(0, temperatures[0])]
        result = [0]

        for i in range(1, len(temperatures)):
            result.append(0)
            if temperatures[i] > aux_stack[-1][1]:
                while aux_stack and temperatures[i] > aux_stack[-1][1]:
                    result[aux_stack[-1][0]] = i - aux_stack[-1][0]
                    aux_stack.pop()
            aux_stack.append((i, temperatures[i]))
            
            print(result)
            print(aux_stack)
        return result