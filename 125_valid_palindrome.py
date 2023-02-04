"""
https://leetcode.com/problems/valid-palindrome/
"""

'''
Thought process:
(Brute Force)
-First, remove all non-alphanumeric characters from the string
-Reverse the string
-Compare original and the reversed string
  -If match, then return true, it is a palindrome
  -Else, return false (not a palindrome)

Not needed...:
-Make all characters lowercase, if they are letters
-Compare the first and last characters of the string
  -If the characters are equal, move to the inner character from both sides
  -If the characters are not equal, return false (not a palindrome)
  -Continue until either:
    -the indices are 1 number away from each other (even number of characters)(then return true, it is a palindrome) or
    -the indices are the same (odd number of characters)(then return true, it is a palindrome)
'''
# To run file: python 125_valid_palindrome.py
# To run doctest: python -m doctest 125_valid_palindrome.py -v
def isPalindrome(input_string: str) -> bool:
    """
    Given a string, see if it is a palindrome.

    :param: str
    :return: bool

    >>> isPalindrome("A man, a plan, a canal: Panama")
    True
    >>> isPalindrome("race a car")
    False
    >>> isPalindrome(" ")
    True
    """
    alpha_num_string = "".join(char.lower() for char in input_string if char.isalnum())
    alpha_num_string_reverse = alpha_num_string[::-1]

    if alpha_num_string == alpha_num_string_reverse:
      return True
    else:
      return False