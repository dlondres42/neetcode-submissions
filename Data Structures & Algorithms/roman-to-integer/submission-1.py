class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        
        for i, char in enumerate(s):
            result += roman_dict[char]
            print(result)
            if result and roman_dict[s[i - 1]] < roman_dict[char] and i > 0:
                result -=  2 * roman_dict[s[i - 1]] 
            print(result)
                
           
        return result