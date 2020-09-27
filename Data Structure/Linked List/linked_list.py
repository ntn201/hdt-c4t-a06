class Node:
    def __init__(self,content,next_node=None):
        self.content = content
        self.next = next_node
    def __str__(self):
        return str(self.content)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return "<<E>>"
        current = self.head
        res = ""
        while current != None:
            res += str(current) + "->"
            current = current.next
        return res[:-2]

    def add_first(self,content):
        new_node = Node(content,self.head)
        self.head = new_node

    def remove_first(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            return temp

    def add_last(self,content):
        if self.head != None:
            new_node = Node(content)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        else:
            self.add_first(content)

    def remove_last(self):
        if self.head != None:
            if self.head.next == None:
                temp = self.head
                self.head = None
                return temp
            else:
                curr = self.head
                while curr.next.next != None:
                    curr = curr.next
                temp = curr.next
                curr.next = None
                return temp
        else:
            return None

    def find(self,content):
        if self.head != None:
            curr = self.head
            while curr != None:
                if curr.content == content:
                    return curr
                curr = curr.next

