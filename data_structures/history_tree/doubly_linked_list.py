class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __str__(self):
        return f"Node({self.data})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = None
        self.length = 0

    def prepend(self, item):
        node = Node(item)
        # Guaranteed to insert
        # Safe to add to length before any observations
        self.length += 1
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at(self, item, idx):
        if idx < 0 or idx > self.length:
            raise IndexError("Out of range")
        if idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return

        curr = self.head
        for i in range(self.length):
            if curr is not None:
                if i+1 == idx:
                    new_node = Node(item)
                    new_node.next = curr.next
                    new_node.prev = curr
                    curr.next.prev = new_node
                    curr.next = new_node
                    self.length += 1
                    return
                curr = curr.next
            else:
                return
        

    def append(self, item):
        self.length += 1
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.curr = new_node
    
    def undo(self):
        if self.curr and self.curr.prev:
            self.curr = self.curr.prev
    
    def redo(self):
        if self.curr is None and self.head is not None:
            self.curr = self.head
        if self.curr and self.curr.next:
            self.curr = self.curr.next
    
    def trim_redo_history(self):
        if self.curr:
            self.curr.next = None
            self.tail = self.curr

    def remove(self, item):
        curr = self.head
        while curr is not None:
            if curr.data == item:
                if curr == self.head and curr == self.tail:
                    self.head = self.tail = None
                elif curr == self.head:
                    self.head = curr.next
                    self.head.prev = None
                elif curr == self.tail:
                    self.tail = curr.prev
                    self.tail.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                self.length -= 1
                return
            curr = curr.next
        

    def remove_at(self, idx):
        found = self.get_idx(idx)
        if found == None:
            return

        if self.head == found and self.tail == found:
            self.head = self.tail = None
        elif self.head == found:
            self.head = found.next
            self.head.prev = None
        elif self.tail == found:
            self.tail = found.prev
            self.tail.next = None
        else:
            found.prev.next = found.next
            found.next.prev = found.prev

        self.length -= 1
        

    def remove_last(self):
        if self.length == 0:
            return
        # If last element is being removed
        # Remove all references to it
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1

    def get_idx(self, idx):
        if idx < 0 or idx > self.length-1:
            raise IndexError("Out of bounds")

        if self.length == 0:
            return

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr

    def to_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

    def __str__(self):
        curr = self.head
        res = []
        while curr:
            # Represent empty string nodes with '""'
            res.append('""' if curr.data == '' else str(curr.data))
            curr = curr.next
        # Show only 'None' if the list is empty or the only node is an empty string
        if not res or (len(res) == 1 and res[0] == '""'):
            return 'None'
        res.append('None')
        return ' -> '.join(res)
