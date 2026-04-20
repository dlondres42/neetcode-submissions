class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        aux_map = {}
        for char in magazine:
            if char not in aux_map: aux_map[char] = 1
            else: aux_map[char] += 1

        #print(aux_map)

        for char in ransomNote:
            if char in aux_map and aux_map[char] > 0: aux_map[char] -= 1
            else: return False 

        return True