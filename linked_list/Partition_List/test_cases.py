from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    head = create_linked_list([1, 4, 3, 2, 5, 2])
    x = 3
    expected_output = create_linked_list([1, 2, 2, 4, 3, 5])
    assert linked_list_to_list(solution.partition(head, x)) == linked_list_to_list(expected_output), "Test case 1 failed"

    # Example 2
    head = create_linked_list([2, 1])
    x = 2
    expected_output = create_linked_list([1, 2])
    assert linked_list_to_list(solution.partition(head, x)) == linked_list_to_list(expected_output), "Test case 2 failed"

    print("All test cases passed!")

# Utility functions to create and convert linked lists for testing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == '__main__':
    run_tests()
