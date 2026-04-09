class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        aux_map = {}
        if len(pattern) != len(s.split()): return False
        for key, word in zip(pattern, s.split()):
            print(f"{key}, {word}")
            if key not in aux_map:
                if word in aux_map.values(): return False
                aux_map[key] = word
            else:
                if aux_map[key] != word: return False

        print(aux_map.values())
        
        return True
            