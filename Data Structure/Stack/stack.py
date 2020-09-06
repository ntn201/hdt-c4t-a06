class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        res = ""
        if not self.is_empty():
            for i in range(len(self.items) - 1):
                res += str(self.items[i]) + " "
            res += str(self.items[-1])
        return res

    def push(self,value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    def is_empty(self):
        return /*1
