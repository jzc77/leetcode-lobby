"""
https://leetcode.com/problems/valid-parentheses/
"""

'''
Thought process:
(Brute Force)
-Iterate through each character in the string
-Use 3 variables to keep track of each bracket type, with starting value of 0
-For each open bracket type encountered, add 1 to the respective variable
-For each close bracket type encountered, subtract 1 from the respective variable
-After then end of the string iteration, add up the three variables
    -If final sum is 0, then return true (string is valid)
    -If final sum is not 0, then return false (string is not valid)
'''
# To run file: python 20_valid_parentheses.py
# To run doctest: python -m doctest 20_valid_parentheses.py -v
def isValid(input_string: str) -> bool:
    """
    Given a string of bracket characters, check if all the open brackets have closing brackets in the right order.

    :param: str
    :return: bool

    >>> isValid("()")
    True
    >>> isValid("()[]{}")
    True
    >>> isValid("(]")
    False
    """
    bracket_1 = 0   # ()
    bracket_2 = 0   # []
    bracket_3 = 0   # {}
    for character in input_string:
      if character == "(":
        bracket_1 += 1
      if character == ")":
        bracket_1 -= 1
      if character == "[":
        bracket_2 += 1
      if character == "]":
        bracket_2 -= 1
      if character == "{":
        bracket_3 += 1
      if character == "}":
        bracket_3 -= 1
    return bracket_1 == bracket_2 == bracket_3 == 0


if __name__ == "__main__":
  isValid("()")
