"""
https://leetcode.com/problems/valid-anagram/
"""

'''
Thought process:
Approach 1
-Order both strings alphabetically e.g. use the method sorted(iterable)
-Then loop through both strings and compare each letter
  -If a letter does not match at the same index, return false
  -If the length of the string has been visited, and no returns, then return true

Approach 2
-Put both strings into two lists of letters e.g. [s, t, r, i, n, g, _, 1] and [s, t, r, i, n, g, _, 2]
-Loop through the first string
-For each letter in the first string, loop through each letter in the second string and compare the letters
-If the letters match, remove that letter from the second string list
-If the length of the first string has been visited, AND the second string list is 0, return true
-Else, return false
'''

def valid_anagram(string_1: str, string_2:str):
  sorted_string_1 = sorted(string_1)  # ['a', 'a', 'a', 'g', 'm', 'n', 'r']
  sorted_string_2 = sorted(string_2)  # ['a', 'a', 'a', 'g', 'm', 'n', 'r']
  
  if len(sorted_string_1) != len(sorted_string_2):
    return False

  for index in range(len(sorted_string_1)):
    if sorted_string_1[index] == sorted_string_2[index]:
      continue
    else:
      return False
  return True

print(valid_anagram("rat", "car"))
