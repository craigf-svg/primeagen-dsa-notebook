# A queue using an array as its underlying data structure
class MyQueue():
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)
        return

    def dequeue(self):
        if self.data:
            var1 = self.data.pop(0)
            return var1
        return

    def empty(self):
        if self.data:
            return False
        return True

    def print_queue(self):
        print('Queue', self.data)

    def __str__(self):
        return f'{self.data}'
