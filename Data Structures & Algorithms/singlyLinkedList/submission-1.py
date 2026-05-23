class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        pointer = self.head
        i = 0
        while pointer is not None and i <= index:
            if i == index:
                return pointer["val"]
            pointer = pointer["next_node"]
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = {"val": val, "next_node": None}
        new_node["next_node"] = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = {"val": val, "next_node": None}
        if self.head is None:
            self.head = new_node
            return
        pointer = self.head
        while pointer["next_node"] is not None:
            pointer = pointer["next_node"]
        pointer["next_node"] = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        i = 0
        pointer = self.head
        prev = self.head
        while pointer is not None and i <= index:
            if i == index:
                prev["next_node"] = pointer["next_node"]
                if index == 0:
                    self.head = prev["next_node"]
                return True
            prev = pointer
            pointer = pointer["next_node"]
            i += 1
        return False

    def getValues(self) -> List[int]:
        vals = []
        pointer = self.head
        while pointer is not None:
            vals.append(pointer["val"])
            pointer = pointer["next_node"]
        return vals
        
