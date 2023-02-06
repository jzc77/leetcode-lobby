"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

'''
Thought process:
-Need variable or hash map to keep track of prices visited
-Need variable to keep track of highest difference between prices
'''
# To run file: python 121_best_time_to_buy_and_sell_stock.py
# To run doctest: python -m doctest 121_best_time_to_buy_and_sell_stock.py -v


def maxProfit(prices: list[int]) -> int:
    """
    Given an array of prices, maximize profit by buying lowest priced stock 
    and selling the stock when the price is the highest.

    :param: list of int
    :return: int

    >>> maxProfit([7,1,5,3,6,4])
    5
    >>> maxProfit([7,6,4,3,1])
    0
    """
    left, right = 0, 1
    maxDifference = 0

    while right < len(prices):
        if prices[right] - prices[left] < 0:
            left = right
            right += 1
        else:
            profit = prices[right] - prices[left]
            maxDifference = max(maxDifference, profit)
            right += 1
    return maxDifference

print(maxProfit([7,1,5,3,6,4]))


