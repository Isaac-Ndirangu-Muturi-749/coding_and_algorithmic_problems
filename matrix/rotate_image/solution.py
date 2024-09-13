class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Rotate the matrix layer by layer
        left, right = 0, n - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Save the top-left corner element
                topLeft = matrix[top][left + i]

                # Move bottom-left to top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom-right to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top-right to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move top-left to top-right
                matrix[top + i][right] = topLeft

            # Move to the inner layer
            left += 1
            right -= 1
