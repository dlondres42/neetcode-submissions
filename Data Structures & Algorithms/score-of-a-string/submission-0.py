class Solution:
    # usar ord pega valor ASCII do char
    # para n chars, n - 1 somas
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i-1]) - ord(s[i]))
            print(score)
            
        return score