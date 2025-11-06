# Stack: Last In, First Out (LIFO) data structure where you add/remove elements only from the top.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack():
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.length += 1
            return

        node.prev = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            self.head = None
            return None
        self.length -= 1
        removed = self.head.data
        self.head = self.head.prev
        return removed

    def peek(self):
        if self.head:
            return self.head.data

    def to_string(self):
        current = self.head
        result = ''
        while current:
            result += f"{current.data} -> "
            current = current.prev
        result += "None"
        return result
