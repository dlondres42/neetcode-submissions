class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            if len(pref) > len(word): continue
            # comeca a comparar
            i = 0
            while i < len(pref):
                if pref[i] == word[i]: i += 1
                else: break

            if i == len(pref): result += 1
            
        return result