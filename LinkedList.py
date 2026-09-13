class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Reverse Linked List - O(N) time, O(1) space
def reverse(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Find Middle Node - Fast & Slow Pointers
def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Detect Cycle - Floyd's Algorithm
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False