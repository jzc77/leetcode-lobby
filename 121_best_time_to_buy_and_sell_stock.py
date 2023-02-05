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


def maxProfit(prices: List[int]) -> int:
    """
    Given an array of prices, maximize profit by buying lowest priced stock 
    and selling the stock when the price is the highest.

    :param: list of int
    :return: int

    >>> maxProfit([7,1,5,3,6,4])
    True
    >>> maxProfit("race a car")
    False
    """
