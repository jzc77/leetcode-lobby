"""
https://leetcode.com/problems/reverse-linked-list/
"""

'''
Thought process:
-First, if the head node is empty, return an empty list.
-There needs to be variables to keep track of the current node and the previous node.
-If the next node exists, move the current node to the next node AND keep track of the previous node.
-Keep repeating, until there is no next node (next node does not exist).
-If next node does not exist, take the current node (which should now be at the end), put it into another list (at the beginning).
-Move the current node to the previous node and add it to the new list.
-Keep repeating until there is no previous node.
-Can now return the new list.
'''
# To run file: python 206_reverse_linked_list.py
# To run doctest: python -m doctest 206_reverse_linked_list.py -v

class ListNode:
  def __init__(self, val=0, next=None):
     self.val = val
     self.next = next


def reverseList_usingPointers(head: ListNode) -> ListNode:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    :param: list
    :return: list

    >>> reverseList_usingPointers([1,2,3,4,5])
    [5,4,3,2,1]
    >>> reverseList_usingPointers([1,2])
    [2,1]
    >>> reverseList_usingPointers([])
    []
    """
    prev, current = None, head

    while current:
      temp_next = current.next
      current.next = prev
      prev = current
      current = temp_next
    return prev

if __name__ == "__main__":
  reverseList_usingPointers([1,2,3,4,5])