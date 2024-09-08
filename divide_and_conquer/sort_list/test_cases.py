from solution import Solution, ListNode

# Helper function to create a linked list from a list.
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list.
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def run_tests():
    solution = Solution()

    # Test case 1
    head = create_linked_list([4, 2, 1, 3])
    result = solution.sortList(head)
    assert linked_list_to_list(result) == [1, 2, 3, 4], f"Test case 1 failed: {linked_list_to_list(result)}"

    # Test case 2
    head = create_linked_list([-1, 5, 3, 4, 0])
    result = solution.sortList(head)
    assert linked_list_to_list(result) == [-1, 0, 3, 4, 5], f"Test case 2 failed: {linked_list_to_list(result)}"

    # Test case 3
    head = create_linked_list([])
    result = solution.sortList(head)
    assert linked_list_to_list(result) == [], f"Test case 3 failed: {linked_list_to_list(result)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
