class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pointer = 0
        word2_pointer = 0
        result_string = ""
        while word1_pointer < len(word1) and word2_pointer < len(word2):
            result_string += word1[word1_pointer]
            result_string += word2[word2_pointer]
            word1_pointer += 1
            word2_pointer += 1

        if word1_pointer < len(word1):
            result_string += word1[word1_pointer:]

        if word2_pointer < len(word2):
            result_string += word2[word2_pointer:]

        return result_string