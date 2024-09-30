from solution import Solution

def list_to_linkedlist(lst):
    """Helper function to convert a list into a linked list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(node):
    """Helper function to convert a linked list into a list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def run_tests():
    solution = Solution()

    # Test case 1: Remove the 2nd node from the end
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    n1 = 2
    expected_output1 = [1, 2, 3, 5]
    result1 = solution.removeNthFromEnd(head1, n1)
    assert linkedlist_to_list(result1) == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {linkedlist_to_list(result1)}"
    print("Test case 1 passed")

    # Test case 2: Remove the only node
    head2 = list_to_linkedlist([1])
    n2 = 1
    expected_output2 = []
    result2 = solution.removeNthFromEnd(head2, n2)
    assert linkedlist_to_list(result2) == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {linkedlist_to_list(result2)}"
    print("Test case 2 passed")

    # Test case 3: Remove the last node
    head3 = list_to_linkedlist([1, 2])
    n3 = 1
    expected_output3 = [1]
    result3 = solution.removeNthFromEnd(head3, n3)
    assert linkedlist_to_list(result3) == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {linkedlist_to_list(result3)}"
    print("Test case 3 passed")

if __name__ == '__main__':
    run_tests()
