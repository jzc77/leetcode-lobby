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

# Approach 1
def valid_anagram_approach_1(string_1: str, string_2:str):
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

print(valid_anagram_approach_1("anagram", "nagaram"))

# Approach 2
def valid_anagram_approach_2(string_1: str, string_2:str):
  list_string_1 = list(string_1)  # ['a', 'n', 'a', 'g', 'r', 'a', 'm']
  list_string_2 = list(string_2)  # ['n', 'a', 'g', 'a', 'r', 'a', 'm']
  
  for letter_in_string_1 in list_string_1:
    for letter_in_string_2 in list_string_2:
      if letter_in_string_1 not in list_string_2:
        return False
      if letter_in_string_1 == letter_in_string_2:
        list_string_2.remove(letter_in_string_1)
        break  # break out of second for-loop
    if len(list_string_2) == 0:
      return True

print(valid_anagram_approach_2("anagram", "nagaram"))
