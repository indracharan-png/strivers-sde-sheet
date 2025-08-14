class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        days = len(prices)

        # Set the variable to store the largest profit
        max_profit = 0
        # This stores the highest price stock has ever reached in the future
        max_share_price = 0

        for day in range(days-1, -1, -1):
            # Price at the current day
            current_day_share_price = prices[day]

            # If current day price of share is less than the best/max price we have seen in future
            if current_day_share_price < max_share_price:
                # Profit check
                current_profit = max_share_price - current_day_share_price
                # Consider if this transaction only if it provides more profit
                if current_profit > max_profit:
                    max_profit = current_profit
            else:
                # Current day has more share price than the best/max we seen so far
                max_share_price = current_day_share_price
        
        return max_profit



            
                


        