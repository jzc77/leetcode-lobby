"""
https://leetcode.com/problems/two-sum/
"""
from typing import List
'''
Thought process:
(Brute force)
-Start at the first number in the list and get its index
-Subtract the first number in the list from the target to get a new target
-Go through the rest of the list to find the new target's index and return both indices
-If there is no match, repeat the above steps with the next number in the list
-Continue until an answer is found (the question says that there is exactly one solution)
'''
def two_sum(nums: List[int], target: int) -> List[int]:
  output_list = []
  
  for index_first_number, first_number in enumerate(nums):
    new_target = target - first_number  # e.g. 9-2=7
    for index_second_number, second_number in enumerate(nums[1:], start=1):  # [1:] means start the list at index 1. "start=1" means get the index number of the second list element
      if second_number == new_target:
        output_list.append(index_first_number)
        output_list.append(index_second_number)
        return output_list

#two_sum([2,7,11,15], 9)
#two_sum([3,3], 6)
two_sum([3, -10, 2, 19], 9)