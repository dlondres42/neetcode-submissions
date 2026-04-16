class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        aux_map = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in aux_map:aux_map[char] += 1

        aux_map['l'] //= 2
        aux_map['o'] //= 2

        return min(aux_map.values())