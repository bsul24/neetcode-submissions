# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        new_head = None
        cur = None
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if not new_head:
                if list1.val <= list2.val:
                    new_head = list1
                    cur = list1
                    cur1 = cur1.next
                else:
                    new_head = list2
                    cur = list2
                    cur2 = cur2.next
            elif cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
        if cur1:
            while cur1:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
        elif cur2:
            while cur2:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        return new_head