class Stack:
    def __init__(self, maxsize):
        self.items = []
        self.max_items = maxsize

    def push(self, n):
        if self.get_size() == self.max_items:
            raise OverflowError(f"Stack cannot contain more than {self.max_items} items.")

        self.items.append(n)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return f'Stack is empty. Nothing to pop.'

    def peek(self):
        # return self.items[-1]
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []
        # if len(self.items) == 0:
        #     return True
        # else:
        #     return False

    def get_size(self) -> int:
        return len(self.items)


s = Stack(5)
s.push(5)
s.push(-10)
print(s.peek())
print(s.pop())
print(s.pop())
# print(s.peek())
print(s.isEmpty())