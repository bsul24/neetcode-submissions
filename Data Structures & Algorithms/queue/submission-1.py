class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def append(self, value: int) -> None:
        node = ListNode(value, self.right.prev, self.right)
        node.prev.next = node
        self.right.prev = node

    def appendleft(self, value: int) -> None:
        node = ListNode(value, self.left, self.left.next)
        node.next.prev = node
        self.left.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.right.prev
        node.prev.next = self.right
        self.right.prev = node.prev
        return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.left.next
        node.next.prev = self.left
        self.left.next = node.next
        return node.val
