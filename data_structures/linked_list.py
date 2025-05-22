# A list of nodes where each node contains a reference to the 'next' node on the list,
# Simple data structure for efficient insertions or deletions.
# [Linked List Notes](notes/linked_lists.md)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(data)

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_matched_first(self, dataToDelete):
        if self.head == None:
            return
        if self.head.data == dataToDelete:
            self.head = self.head.next
        return

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
        return

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"
