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
        return self.items == []

s = Stack()
assert(s.is_empty())
assert(hasattr(s, "items"))
assert(hasattr(s, "push"))
assert(hasattr(s, "pop"))
assert(hasattr(s, "is_empty"))

s.push(5)
assert(not s.is_empty())
assert(s.__str__() == "5")

s.push(7)
assert(not s.is_empty())
assert(s.__str__() == "5 7")

s.push(-1)
assert(not s.is_empty())
assert(s.__str__() == "5 7 -1")

x = s.pop()
assert(not s.is_empty())
assert(s.__str__() == "5 7")
assert(x == -1)

x = s.pop()
assert(not s.is_empty())
assert(s.__str__() == "5")
assert(x == 7)

s.push(11)
assert(not s.is_empty())
assert(s.__str__() == "5 11")

x = s.pop()
assert(not s.is_empty())
assert(s.__str__() == "5")
assert(x == 11)

x = s.pop()
assert(s.is_empty())
assert(s.__str__() == "")
assert(x == 5)


s.push(6)
s.push(7)
assert(s.__str__() == "6 7")
s.clear()
assert(s.__str__() == "")
assert(s.is_empty())
# 5 4 3 2 1