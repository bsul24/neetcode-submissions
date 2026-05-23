class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        while index > 0 and cur:
            cur = cur.next
            index -= 1
        if cur:
            return cur.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if self.tail == self.head:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        cur = self.head
        while index > 0 and cur:
            cur = cur.next
            index -= 1
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False    

    def getValues(self) -> List[int]:
        vals = []
        cur = self.head.next
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
        
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# ll = LinkedList()
# ll.insertTail(1)
# ll.insertTail(2)
# print(ll.getValues())
