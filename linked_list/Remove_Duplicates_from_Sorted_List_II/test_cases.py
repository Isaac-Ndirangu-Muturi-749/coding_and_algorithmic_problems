from solution import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper function to create a linked list from a Python list
    @staticmethod
    def from_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list to a Python list
    def to_list(self):
        lst = []
        current = self
        while current:
            lst.append(current.val)
            current = current.next
        return lst

def run_tests():
    solution = Solution()

    # Test case 1
    head1 = ListNode.from_list([1, 2, 3, 3, 4, 4, 5])
    expected_output1 = [1, 2, 5]
    result1 = solution.deleteDuplicates(head1)
    assert result1.to_list() == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1.to_list()}"
    print("Test case 1 passed")

    # Test case 2
    head2 = ListNode.from_list([1, 1, 1, 2, 3])
    expected_output2 = [2, 3]
    result2 = solution.deleteDuplicates(head2)
    assert result2.to_list() == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2.to_list()}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
