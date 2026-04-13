# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        self.sort(pairs, 0, len(pairs) - 1)

        return pairs

    def sort(self, pairs, s, e):
        if s >= e:
            return pairs
        mid = (s + e) // 2

        self.sort(pairs, s, mid)
        self.sort(pairs, mid + 1, e)
        self.merge(pairs, s, mid, e)
    
    def merge(self, pairs, s, m ,e):
        left_array = pairs[s: m + 1]
        right_array = pairs[m + 1: e + 1]
        k = s 
        l = r = 0
        
        while l < len(left_array) and r < len(right_array):
            if left_array[l].key <= right_array[r].key:
                pairs[k] = left_array[l]
                l += 1
            else:
                pairs[k] = right_array[r]
                r += 1
            k += 1

        pairs[k: e + 1] = left_array[l:] + right_array[r:]
