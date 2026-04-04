class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        temp_result = 0 
        for number in nums:
            if number:
                temp_result += 1
            else:
                if temp_result > result:
                    result = temp_result
                temp_result = 0
    
        return temp_result if temp_result > result else result