class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aux_dict = {}
        result = []
        for word in strs: #O(len(strs))
            encoding = [0 for _ in range(26)]
            for char in word: # O(word)
                index = ord(char) - ord('a')
                encoding[index] += 1
                
            encoding = tuple(encoding)
            if encoding not in aux_dict: aux_dict[encoding] = [word]
            else: aux_dict[encoding].append(word)

        for key in aux_dict.keys(): #O(len(strs))
            result.append(aux_dict[key])

        # O(len(strs) * len(word))

        return result
        
            
            