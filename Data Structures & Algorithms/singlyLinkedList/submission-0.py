class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next  # Link to current first node (or None)
        self.head.next = new_node 

        if new_node.next is None: # If list was empty
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head # start at dummy node to have access to previous nodes
        
        # Move curr to the node BEFORE the one we want to remove
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # check if the node to remove exists
        if curr and curr.next:
            # Update tail if we're removing the last node
            if curr.next == self.tail:
                self.tail = curr
            # remove the node
            curr.next = curr.next.next
            return True
        
        return False
        
    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
