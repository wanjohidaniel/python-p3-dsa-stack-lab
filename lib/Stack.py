class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return False  # Modify push to return False if the stack is full
        self.items.append(item)
        return True

    def pop(self):
        if self.isEmpty():
            return None  # Modify pop to return None if the stack is empty
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None  # Modify peek to return None if the stack is empty
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return self.items[::-1].index(target)
        except ValueError:
            return -1
