# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from utils import ListNode, create_linked_list

def r(head):
  cur = head
  while cur:
    while cur.next and cur.next.val == cur.val:
      cur.next = cur.next.next
    cur = cur.next
  return head

dummyHead = create_linked_list([1, 1, 1, 2, 3, 4, 4, 9])

head = r(dummyHead)

while head:
  print(head.val)
  head = head.next