"""
https://leetcode.com/problems/binary-search/
"""

'''
Thought process:
(Binary search must be implemented, as stated in the problem)
-Start search at middle of list.
-If the target is more than middle int, start another binary search to the right. Else, search left.
-Continue until target is found or does not exist.
'''
# To run file: python 704_binary_search.py
# To run doctest: python -m doctest 704_binary_search.py -v

import math

def search(nums: list[int], target: int) -> int:
    """
    Given a list of integers, find the index of the target value.

    :param: list
    :return: int

    >>> search([-1,0,3,5,9,12], 9)
    4
    >>> search([-1,0,3,5,9,12], 2)
    -1
    """
    left, right = 0, len(nums) - 1  # 0, 5
    list_middle = math.floor((left + right) / 2)  # 2
    
    while list_middle > 0:
      if list_middle == target:
        return list_middle
      else:
        if list_middle < target:
          left = list_middle + 1  # Need to move left pointer to right half of original list
        else:
          right = list_middle - 1 # Need to move right pointer to left half of original list

    return -1 # Target not found in original list




if __name__ == "__main__":
  search([-1,0,3,5,9,12], 9)


    # if list_length % 2 == 0:
    #   list_middle = nums[math.floor((len(nums) / 2) - 1)]   # middle of nums list for even list length
    # else:
    #   list_middle = nums[math.floor((len(nums) / 2))]       # middle of nums list for odd list length