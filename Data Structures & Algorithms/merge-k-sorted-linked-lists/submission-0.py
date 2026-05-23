# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None

        for i in range(len(lists)):
            if res is None:
                res = lists[i]
            else:
                res = self.merge(res, lists[i])
        return res

    def mergeKListsHelper(self, lists, s, e):
        if e - s + 1 <= 1:
            return lists

        m = (s + e) // 2

        left = self.mergeKListsHelper(lists, s, m)
        right = self.mergeKListsHelper(lists, m+1, e)

        res = self.merge(left, right)

        
    def merge(self, L, R):
        res = None
        head = None
        while L and R:
            if L.val <= R.val:
                if res is None:
                    res = ListNode(L.val)
                    head = res
                else:
                    res.next = ListNode(L.val)
                    res = res.next
                L = L.next
            else:
                if res is None:
                    res = ListNode(R.val)
                    head = res
                else:
                    res.next = ListNode(R.val)
                    res = res.next
                R = R.next
        
        while L:
            res.next = ListNode(L.val)
            res = res.next
            L = L.next
        while R:
            res.next = ListNode(R.val)
            res = res.next
            R = R.next
        return head