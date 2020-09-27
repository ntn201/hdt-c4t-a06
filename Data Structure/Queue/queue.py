class Queue:
    def __init__(self,capacity):
        self.items = []
        self.capacity = capacity

    def __str__(self):
        res = ""
        if not self.is_empty():
            for i in range(len(self.items) - 1):
                res += str(self.items[i]) + " "
            res += str(self.items[-1])
        return res

    def insert(self,value):
        self.items.insert(0,value)


    def remove(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def is_full(self):
        return len(self.items) >= self.capacity