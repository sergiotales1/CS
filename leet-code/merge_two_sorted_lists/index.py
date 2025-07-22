# https://leetcode.com/problems/merge-two-sorted-lists/

from utils import ListNode, create_linked_list

list1_head = create_linked_list([1, 2, 4])
list2_head = create_linked_list([1, 3, 4])

def merge_sort(l1, l2):
  sortedList = ListNode()
  sortedListTail = sortedList
  
  while l1 and l2:
    if l1.val < l2.val:
       sortedListTail.next = l1
       l1 = l1.next
    else:
       sortedListTail.next = l2
       l2 = l2.next

  if l1:
      while l1:
        sortedListTail.next = l1
        l1 = l1.next
  elif l2:
      while l2:
        sortedListTail.next = l2
        l2 = l2.next
  
  return sortedList.next
    

merge_sort(list1_head, list2_head)