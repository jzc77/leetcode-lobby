import unittest
from contains_duplicate import containsDuplicate

"""
Run all tests in the command line with the command:
python -m unittest test_contains_duplicate

or

python -m unittest
"""

class Test_contains_duplicate(unittest.TestCase):
  def test_contains_duplicate(self):
    # Tests arrays that contains duplicate elements
    self.assertEqual(containsDuplicate([1,2,3,1]), True)

  def test_does_not_contains_duplicate(self):
    # Tests arrays that do not contains duplicate elements
    self.assertEqual(containsDuplicate([1,2,3,4]), False)

  def test_contains_duplicate_long(self):
    # Tests longer arrays that contains duplicate elements
    self.assertEqual(containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)