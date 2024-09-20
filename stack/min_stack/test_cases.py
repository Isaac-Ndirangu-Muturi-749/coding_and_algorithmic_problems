from solution import MinStack

def run_tests():
    # Test case based on the given example
    minStack = MinStack()

    # Step 1: Push -2 onto the stack
    minStack.push(-2)

    # Step 2: Push 0 onto the stack
    minStack.push(0)

    # Step 3: Push -3 onto the stack
    minStack.push(-3)

    # Step 4: Get minimum (should be -3)
    result1 = minStack.getMin()
    assert result1 == -3, f"Test case failed at getMin: Expected -3, got {result1}"

    # Step 5: Pop the top element (-3)
    minStack.pop()

    # Step 6: Get the top element (should be 0)
    result2 = minStack.top()
    assert result2 == 0, f"Test case failed at top: Expected 0, got {result2}"

    # Step 7: Get the minimum element (should be -2)
    result3 = minStack.getMin()
    assert result3 == -2, f"Test case failed at getMin: Expected -2, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
