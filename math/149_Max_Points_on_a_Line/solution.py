from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:


        def find_Line(x0, y0, x1, y1):
            if y0 == y1:  # Horizontal line
                return 0, y0
            if x0 == x1:  # Vertical line
                return x0, None
            else:  # General line (slope-intercept form)
                slope = (y1 - y0) / (x1 - x0)
                intercept = y0 - slope * x0
                return slope, intercept

        if len(points) == 1:
            return 1

        # Dictionary to store points for each line
        lines = defaultdict(lambda: set())

        # Iterate through all pairs of points
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x0, y0 = points[i]
                x1, y1 = points[j]
                line = find_Line(x0, y0, x1, y1)
                lines[line].add(i)
                lines[line].add(j)

        # Find the maximum points on a single line
        return max(len(lines[line]) for line in lines)
