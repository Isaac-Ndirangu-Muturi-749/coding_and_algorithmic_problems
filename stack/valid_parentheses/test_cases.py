from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Simple valid parentheses
    s1 = "()"
    assert solution.isValid(s1) == True, f"Test case 1 failed: {s1}"

    # Test case 2: Mixed valid parentheses
    s2 = "()[]{}"
    assert solution.isValid(s2) == True, f"Test case 2 failed: {s2}"

    # Test case 3: Invalid closing bracket
    s3 = "(]"
    assert solution.isValid(s3) == False, f"Test case 3 failed: {s3}"

    # Test case 4: Valid nested parentheses
    s4 = "([])"
    assert solution.isValid(s4) == True, f"Test case 4 failed: {s4}"

    # Test case 5: Extra closing bracket
    s5 = "([)]"
    assert solution.isValid(s5) == False, f"Test case 5 failed: {s5}"

    # Test case 6: Only opening brackets
    s6 = "((("
    assert solution.isValid(s6) == False, f"Test case 6 failed: {s6}"

    # Test case 7: Only closing brackets
    s7 = ")))"
    assert solution.isValid(s7) == False, f"Test case 7 failed: {s7}"

    # Test case 8: Empty string
    s8 = ""
    assert solution.isValid(s8) == True, f"Test case 8 failed: {s8}"

    # Test case 9: Complex valid case
    s9 = "{[()()]}"
    assert solution.isValid(s9) == True, f"Test case 9 failed: {s9}"

    # Test case 10: Complex invalid case
    s10 = "{[(])}"
    assert solution.isValid(s10) == False, f"Test case 10 failed: {s10}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
