"""
https://leetcode.com/problems/valid-palindrome/
"""

'''
Thought process:
(Brute Force)
-First, remove all non-alphanumeric characters from the string
-Compare the first and last characters of the string
  -If the characters are equal, move to the inner character from both sides
  -If the characters are not equal, return false (not a palindrome)
  -Continue until either:
    -the indices are 1 number away from each other (even number of characters)(then return true, it is a palindrome) or
    -the indices are the same (odd number of characters)(then return true, it is a palindrome)
'''