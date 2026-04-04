class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}
        for char in s:
            if not char in charDict: charDict[char] = 1
            else: charDict[char] += 1

        print(charDict)
        for char in t:
            if char in charDict:
                charDict[char] -= 1
                if charDict[char] == 0: del charDict[char]
            else: charDict[char] = 1
        
        print(charDict)
        return False if charDict else True