class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # Split the input path by "/"
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                # Ignore empty parts or current directory
                continue
            elif part == "..":
                if stack:
                    stack.pop()  # Go up one directory level
            else:
                stack.append(part)  # Add directory/file name to stack

        # Join the stack to form the simplified canonical path
        canonical_path = "/" + "/".join(stack)

        return canonical_path
