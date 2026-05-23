class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
    
    def get(self, index: int) -> int:
        cur = self.dummy.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            return cur.val
        return -1

    def insertHead(self, val: int) -> None:
            
        node = ListNode(val)
        if self.dummy == self.tail:
            self.tail = node
        node.next = self.dummy.next
        self.dummy.next = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.dummy == self.tail:
            return self.insertHead(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        if self.dummy.next:
            cur = self.dummy.next
            prev = self.dummy
            while cur and index > 0:
                cur = cur.next
                prev = prev.next
                index -= 1
            if cur and index == 0:
                if cur == self.tail:
                    self.tail = prev
                prev.next = prev.next.next
                return True
            return False
        return False

    def getValues(self) -> List[int]:
        vals = []
        cur = self.dummy.next
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
