from solution import Solution, ListNode

def run_tests():
    solution = Solution()

    # Test case 1
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Create linked list [1 -> 2 -> 3 -> 4 -> 5]
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)

    # Call the method and get output
    output1 = solution.reverseBetween(head1, 2, 4)

    # Collect output as a list for easy comparison
    result1 = []
    while output1:
        result1.append(output1.val)
        output1 = output1.next
    print(f"Test case 1 output: {result1} (Expected: [1, 4, 3, 2, 5])")

    # Test case 2
    # Input: head = [5], left = 1, right = 1
    head2 = ListNode(5)

    # Call the method and get output
    output2 = solution.reverseBetween(head2, 1, 1)

    # Collect output as a list for easy comparison
    result2 = []
    while output2:
        result2.append(output2.val)
        output2 = output2.next
    print(f"Test case 2 output: {result2} (Expected: [5])")

if __name__ == '__main__':
    run_tests()
