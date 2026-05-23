class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = self.tail = None
            return True
        i = 0
        cur = self.head
        while i < index - 1 and cur:
            cur = cur.next
            i += 1

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
        



