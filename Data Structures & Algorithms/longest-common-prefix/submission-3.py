class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        if len(strs) == 1: return longest_prefix

        for word in strs[1:]:
            print(longest_prefix)
            if not word: return ""
            for position in range(len(longest_prefix)):
                if position >= len(word) or position >= len(longest_prefix):
                    longest_prefix = longest_prefix[:position]
                    break
                if word[position] != longest_prefix[position]:
                    longest_prefix = longest_prefix[:position]
                    if not longest_prefix:
                        return ""

        return longest_prefix