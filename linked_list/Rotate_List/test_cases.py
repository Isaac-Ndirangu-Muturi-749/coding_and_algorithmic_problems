from solution import Solution

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Utility function to convert a Python list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Utility function to convert a linked list to a Python list
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def run_tests():
    solution = Solution()

    # Example 1
    head = list_to_linkedlist([1,2,3,4,5])
    k = 2
    rotated = solution.rotateRight(head, k)
    assert linkedlist_to_list(rotated) == [4,5,1,2,3], "Test case 1 failed"

    # Example 2
    head = list_to_linkedlist([0,1,2])
    k = 4
    rotated = solution.rotateRight(head, k)
    assert linkedlist_to_list(rotated) == [2,0,1], "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
