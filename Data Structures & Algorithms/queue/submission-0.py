class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def append(self, value: int) -> None:
        node = ListNode(value)
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        self.right.prev = node


    def appendleft(self, value: int) -> None:
        node = ListNode(value, self.left.next, self.left)
        node.next.prev = node
        self.left.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        tmp = self.right.prev
        tmp.prev.next = self.right
        self.right.prev = tmp.prev
        return tmp.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        tmp = self.left.next
        tmp.next.prev = self.left
        self.left.next = tmp.next
        return tmp.val
