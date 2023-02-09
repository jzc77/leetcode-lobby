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

'''
Thought process:
(Using stack)
-Iterate through each character in the string
-Use a list to keep track of open characters put into it
-If a close bracket is encountered, the corresponding open bracket must be 'popped' off from the list
-If the close bracket's corresponding open bracket is not at the end of the brackets list, return false (string is not valid)
-After the end of the string iteration, return true (string is valid)
-This process ensures ordering is correct
'''
def isValid_withOrdering(input_string: str) -> bool:
    """
    Given a string of bracket characters, check if all the open brackets have closing brackets in the right order.

    :param: str
    :return: bool

    >>> isValid_withOrdering("()")
    True
    >>> isValid_withOrdering("()[]{}")
    True
    >>> isValid_withOrdering("(]")
    False
    >>> isValid_withOrdering("([)]")
    False
    >>> isValid_withOrdering("((")
    False
    >>> isValid_withOrdering("[")
    False
    >>> isValid_withOrdering("]")
    False
    """
    brackets_list = []
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']

    for character in input_string:
      if character in open_brackets:
        brackets_list.append(character)
      else:
        if len(brackets_list) == 0:
          return False
        else: 
          # need closed_brackets index of character
          closed_brackets_index_of_character = closed_brackets.index(character)  # 0
          # get open bracket character using above index
          corresponding_open_bracket = open_brackets[closed_brackets_index_of_character]  # (
          if brackets_list[-1] != corresponding_open_bracket:
            return False
          else:
            brackets_list.pop()
    
    if len(brackets_list) == 0:
      return True
    else:
      return False


if __name__ == "__main__":
  # isValid("()")
  isValid_withOrdering("([)]")