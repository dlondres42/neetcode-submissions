class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        if not s: return True
        
        for position in range(0, len(t)):
            if s_pointer + 1 == len(s): return True
            if s[s_pointer] == t[t_pointer]: s_pointer += 1
            t_pointer += 1

        return False