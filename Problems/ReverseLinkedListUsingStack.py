class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ReverseLinkedListUsingStack:
    def reverseLinkedList(self, head):
        stack = []
        temp = head

        # step 1: Push all the node values to the stack first
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        # step 2: Reassign values in reverse order
        temp = head
        while temp:
            temp.data = stack.pop()
            temp = temp.next

        return head
    
def main():
    solver = ReverseLinkedListUsingStack()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    result = solver.reverseLinkedList(head)

    while result is not None:
        print(result.data)
        result = result.next

if __name__ == "__main__":
    main()