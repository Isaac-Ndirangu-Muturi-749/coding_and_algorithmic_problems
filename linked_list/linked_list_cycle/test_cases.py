class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Cycle exists (pos = 1)
    # Linked list: 3 -> 2 -> 0 -> -4 -> (points back to node with value 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle here
    assert solution.hasCycle(node1) == True, "Test case 1 failed"

    # Test case 2: Cycle exists (pos = 0)
    # Linked list: 1 -> 2 -> (points back to node with value 1)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1  # Cycle here
    assert solution.hasCycle(node1) == True, "Test case 2 failed"

    # Test case 3: No cycle (pos = -1)
    # Linked list: 1 -> (no cycle)
    node1 = ListNode(1)
    assert solution.hasCycle(node1) == False, "Test case 3 failed"

    # Test case 4: Empty list
    # Linked list: (None)
    assert solution.hasCycle(None) == False, "Test case 4 failed"

    # Test case 5: Single node without cycle
    # Linked list: 1 -> None
    node1 = ListNode(1)
    node1.next = None
    assert solution.hasCycle(node1) == False, "Test case 5 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
