class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        cur = self.head
        while index > 0:
            if cur.next:
                cur = cur.next
                index -= 1
            else:
                return -1
        return cur.val

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, None)
        new_head.next = self.head
        self.head = new_head
        if self.tail is None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val, None)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        else:
            cur = self.head
            while index > 1:
                if cur.next:
                    cur = cur.next
                    index -= 1
                else:
                    return False
            if cur.next == self.tail:
                cur.next = None
                self.tail = cur
                return True
            elif cur.next is None:
                return False
            else:
                cur.next = cur.next.next
                return True


    def getValues(self) -> List[int]:
        vals = []
        if self.head is None:
            return vals
        cur = self.head
        while cur.next is not None:
            vals.append(cur.val)
            cur = cur.next
        vals.append(cur.val)
        return vals
        
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

ll = LinkedList()
ll.insertHead(3)
ll.insertHead(2)
print(ll.head.next.val)
print(ll.getValues())