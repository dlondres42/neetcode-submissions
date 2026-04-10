class Solution:
    def minOperations(self, logs: List[str]) -> int:
        aux_stack = []

        for log in logs:
            if log == '../' and aux_stack:
                aux_stack.pop()
            elif log == './' or (log == '../' and not aux_stack):
                continue
            else:
                aux_stack.append(log)

        return len(aux_stack)
            