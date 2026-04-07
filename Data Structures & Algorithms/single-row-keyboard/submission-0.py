class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        aux_map = {}
        result = 0
        for i, letter in enumerate(keyboard):
            aux_map[letter] = i

        print(aux_map)
        
        i = 0
        j = 1
        result = aux_map[word[i]]
        while j < len(word):
            print(f"j {word[j]}, i {word[i]}")
            intermediary_result = abs(aux_map[word[j]] - aux_map[word[i]])
            print(intermediary_result)
            result += intermediary_result
            i += 1
            j += 1
        

        return result