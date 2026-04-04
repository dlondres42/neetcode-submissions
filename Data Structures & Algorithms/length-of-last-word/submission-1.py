# fazendo operacao inplace
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        last_word_len = 0
        while i >= 0:
            if s[i] == ' ' and last_word_len:
                return last_word_len
            
            if s[i] != ' ':
                last_word_len += 1
            
            i -= 1

        return last_word_len