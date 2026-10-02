class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
class ReverseLinkedListIterative:
    def reverse_list(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to the current node
            current = next_node       # Move to the next node

        return prev
    
def main():
    solver = ReverseLinkedListIterative()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    result = solver.reverse_list(head)

    while result is not None:
        print(result.value)
        result = result.next

if __name__ == "__main__":
    main()