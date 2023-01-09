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

'''
Thought process:
(Dictionary)
-Iterate through the list of numbers and store the number as keys in a dictionary
-Going through the list of numbers, check to see if the target minus current number equals a key in the dictionary
-If so, stop the iteration and return current number's index AND the key's value (which is the index of the number 
(in which the number/key adds to the current number to equal the target)
-If not, store the number's index as values, and continue iterating
'''
def two_sum_approach_2(nums: List[int], target: int) -> List[int]:
  nums_index_dict = {}
  
  for index, num in enumerate(nums):
    potential_key = target - num
    if potential_key in nums_index_dict.keys():
      return([index, nums_index_dict[potential_key]])
    nums_index_dict[num] = index
    # need to move this down here or else it will cause accidental num (e.g. 3 in index 0) and the added potential_key
    # (e.g. the same 3, with corresponding value of 0) to add up to the target (e.g. 6), returning the incorrect output (e.g. [0, 0])

# Example dictionaries:
# dict = {
#   3: 0,
#   2: 1,
#   4: 2
# }

# dict = {
#   3: 0,
#   -10: 1,
#   2: 2,
#   19: 3,
# }
