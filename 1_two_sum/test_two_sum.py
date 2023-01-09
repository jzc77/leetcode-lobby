import unittest
import itertools
from two_sum import two_sum, two_sum_approach_2

"""
Run all tests in the command line with the command:
python -m unittest test_two_sum

or

python -m unittest
"""

class Test_two_sum(unittest.TestCase):
  def test_contains_positive_integers_in_order(self):
    # Tests arrays that contains positive integers in order
    self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

  def test_contains_positive_integers_not_in_order(self):
    # Tests arrays that contains positive integers not in order
    self.assertEqual(two_sum([3,2,4], 6), [1, 2])

  def test_contains_same_positive_integers(self):
    # Tests arrays that contain the same positive integers
    self.assertEqual(two_sum([3,3], 6), [0, 1])

  def test_contains_negative_integers(self):
    # Tests arrays that contains a negative integer
    self.assertEqual(two_sum([3, -10, 2, 19], 9), [1, 3])

class Test_two_sum_approach_2(unittest.TestCase):
  def test_contains_positive_integers_in_order(self):
    # Tests arrays that contains positive integers in order
    self.assertEqual(two_sum_approach_2([2, 7, 11, 15], 9), [1, 0])

  def test_contains_positive_integers_not_in_order(self):
  # Tests arrays that contains positive integers not in order
    self.assertEqual(two_sum_approach_2([3,2,4], 6), [2, 1])

  def test_contains_same_positive_integers(self):
    # Tests arrays that contain the same positive integers
    self.assertEqual(two_sum_approach_2([3,3], 6), [1, 0])

  def test_contains_negative_integers(self):
    # Tests arrays that contains a negative integer
    self.assertEqual(two_sum_approach_2([3, -10, 2, 19], 9), [3, 1])