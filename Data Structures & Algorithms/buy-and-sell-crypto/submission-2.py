class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        l = 0
        r = 1
        while r < len(prices) and l < r:
            temp_total_profit = max(prices[r] - prices[l], 0)
            if temp_total_profit > 0:
                total_profit = max(temp_total_profit, total_profit)
                r += 1
            else:
                l += abs(l - r)
                r += 1
            print(f"end: {total_profit}, l: {l},r: {r}")
            

        return total_profit