class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return "Stack is Empty"
        
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def peek(self):
        if self.top is None:
            return "Stack Empty"
        return self.top.data
    
    def isEmpty(self):
        return self.top is None