from solution import Solution

def run_tests():
    solution = Solution()

    # Test cases with assertions
    assert solution.simplifyPath("/home/") == "/home", "Test case 1 failed"
    assert solution.simplifyPath("/home//foo/") == "/home/foo", "Test case 2 failed"
    assert solution.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures", "Test case 3 failed"
    assert solution.simplifyPath("/../") == "/", "Test case 4 failed"
    assert solution.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d", "Test case 5 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
