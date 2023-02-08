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

See second implementation:
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

## TODO: Implement the other way to solve this question (don't use built-in python methods)
## Note: need two functions
def isPalindrome_usingPointers(input_string: str) -> bool:
    """
    Given a string, see if it is a palindrome.

    :param: str
    :return: bool

    >>> isPalindrome_usingPointers("A man, a plan, a canal: Panama")
    True
    >>> isPalindrome_usingPointers("race a car")
    False
    >>> isPalindrome_usingPointers(" ")
    True
    """
    left, right = 0, len(input_string) - 1
    
    while left < right:
      if isAlphaNum(input_string[left]) and isAlphaNum(input_string[right]):  # both comparing characters are alphanumeric
        if input_string[left].lower() == input_string[right].lower():
          left += 1
          right -= 1
        else:
          return False  # once comparing characters are not matching, return false (the input string is not a palindrome)
      else:
        if isAlphaNum(input_string[left]) == False:
          left += 1
        if isAlphaNum(input_string[right]) == False:
          right -= 1
    return True


def isAlphaNum(character: str):
  isAlphaUpperCase = ord(character) >= ord('A') and ord(character) <= ord('Z')
  isAlphaLowerCase = ord(character) >= ord('a') and ord(character) <= ord('z') 
  isNum = ord(character) >= ord('0') and ord(character) <= ord('9') 
  return isAlphaUpperCase or isAlphaLowerCase or isNum

# print(isPalindrome_usingPointers("A man, a plan, a canal: Panama"))
# print(isPalindrome_usingPointers("race a car"))
# print(isPalindrome_usingPointers(" "))