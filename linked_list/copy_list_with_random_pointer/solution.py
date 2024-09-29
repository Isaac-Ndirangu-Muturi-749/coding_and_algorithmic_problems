# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            if not head:
                return None

            # Step 1: Create a hashmap to map original nodes to their copies
            old_to_new = {}

            # First pass: Create copies of each node and map them
            current = head
            while current:
                old_to_new[current] = Node(current.val)
                current = current.next

            # Second pass: Assign next and random pointers
            current = head
            while current:
                if current.next:
                    old_to_new[current].next = old_to_new[current.next]
                if current.random:
                    old_to_new[current].random = old_to_new[current.random]
                current = current.next

            # Return the head of the copied linked list
            return old_to_new[head]
