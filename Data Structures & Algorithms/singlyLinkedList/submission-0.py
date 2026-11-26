class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        curr = self.head.next
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val=val, next_node=self.head.next)
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index < 0:
            return False

        count = 0
        prev = self.head
        curr = self.head.next
        while curr and count < index:
            prev = curr
            curr = curr.next
            count += 1

        if not curr:
            return False

        prev.next = curr.next
        if curr == self.tail:
            self.tail = prev
        return True

    def getValues(self) -> list[int]:
        results = []
        curr = self.head.next
        while curr:
            results.append(curr.val)
            curr = curr.next
        return results