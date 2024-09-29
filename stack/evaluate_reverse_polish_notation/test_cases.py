from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    tokens = ["2","1","+","3","*"]
    output = solution.evalRPN(tokens)
    print(f"Test case 1: {output} == 9")

    # Test case 2
    tokens = ["4","13","5","/","+"]
    output = solution.evalRPN(tokens)
    print(f"Test case 2: {output} == 6")

    # Test case 3
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    output = solution.evalRPN(tokens)
    print(f"Test case 3: {output} == 22")

if __name__ == '__main__':
    run_tests()
