'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy and a different day in the future to sell.
Return the maximum profit. If no profit is possible, return 0.

Example 1
Input: prices = [7,    1,    5,    3,    6,    4]
                7,0    1,0   1,4   1,2   1,5   1,5
Output: 5
Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6)
Profit = 6 - 1 = 5
(Not 7-1=6 because you must buy before selling)
'''

def find(prices: list) -> int:
    min_price=float('inf')
    max_profit=0
    for i in prices:
        min_price=min(min_price, i)
        max_profit=max(max_profit, i-min_price)
    return max_profit


prices = [7,    1,    5,    3,    6,    4]
print(find(prices))