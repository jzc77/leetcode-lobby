"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List
'''
Thought process:

-Go through each element in nums
-For each element, check if it's already in a unique list
  - If not in the unique list, put it into the unique list 
  - If already in the unique list, return true (for containing duplicates in the original list)
-If end of original list is reached, return false (for not containing duplicates in the original list)
'''
def containsDuplicate(nums: List[int]) -> bool:
  unique_list = []
  for element in nums:
    if element not in unique_list:
      unique_list.append(element)
    else:
      return True
  return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


