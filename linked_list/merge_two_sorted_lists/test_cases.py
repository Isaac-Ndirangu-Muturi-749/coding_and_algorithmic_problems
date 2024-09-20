from solution import Solution
from solution import ListNode  # Assuming ListNode is defined in the solution file

def list_to_linked_list(lst):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    """Helper function to convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def run_tests():
    solution = Solution()

    # Test case 1
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    result1 = solution.mergeTwoLists(list1, list2)
    expected1 = [1, 1, 2, 3, 4, 4]
    assert linked_list_to_list(result1) == expected1, f"Test case 1 failed: Expected {expected1}, got {linked_list_to_list(result1)}"

    # Test case 2
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    result2 = solution.mergeTwoLists(list1, list2)
    expected2 = []
    assert linked_list_to_list(result2) == expected2, f"Test case 2 failed: Expected {expected2}, got {linked_list_to_list(result2)}"

    # Test case 3
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    result3 = solution.mergeTwoLists(list1, list2)
    expected3 = [0]
    assert linked_list_to_list(result3) == expected3, f"Test case 3 failed: Expected {expected3}, got {linked_list_to_list(result3)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
