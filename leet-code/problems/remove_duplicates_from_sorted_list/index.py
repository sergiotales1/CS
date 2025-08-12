# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from utils import ListNode, create_linked_list

list1_head = create_linked_list([1, 1, 2, 3, 3])

def i(head):
  cur = head
  while cur:
    while cur.next and cur.next.val == cur.val:
      cur.next = cur.next.next
    cur = cur.next
  return head

head = i(list1_head)

while head:
  print(head.val)
  head = head.next

