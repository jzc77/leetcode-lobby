import unittest
from valid_anagram import valid_anagram_approach_1, valid_anagram_approach_2

"""
Run all tests in the command line with the command:
python -m unittest test_valid_anagram

or

python -m unittest
"""

class Test_valid_anagram(unittest.TestCase):
  def test_valid_anagram_approach_1(self):
    # Tests strings that are anagrams of each other using approach 1
    self.assertEqual(valid_anagram_approach_1("anagram", "nagaram"), True)

  def test_is_not_valid_anagram_approach_1(self):
    # Tests strings that are not anagrams of each other using approach 1
    self.assertEqual(valid_anagram_approach_1("rat", "car"), False)
  def test_valid_anagram_approach_2(self):
    # Tests strings that are anagrams of each other using approach 2
    self.assertEqual(valid_anagram_approach_2("anagram", "nagaram"), True)

  def test_is_not_valid_anagram_approach_2(self):
    # Tests strings that not are anagrams of each other using approach 2
    self.assertEqual(valid_anagram_approach_2("rat", "car"), False)