To solve the problem of finding the maximum number of points that lie on the same straight line, we can use a hashmap-based approach to count points that share the same slope with a given reference point. Here's how we can implement the solution:


---

Approach:

1. Iterate through each point as a reference point:

For each point in the list, treat it as a reference point, and calculate the slope between it and every other point.

Use a hashmap to count how many points share the same slope with the reference point.



2. Calculate the slope:

The slope between two points  and  is calculated as:




\text{slope} = \frac{y2 - y1}{x2 - x1}

3. Handle edge cases:

Points that overlap (same coordinates) should be tracked separately.

Vertical lines should be handled as a special case where the denominator is zero.



4. Update the maximum:

For each reference point, calculate the maximum count of points that share the same slope, including overlapping points.



5. Return the result:

Iterate over all reference points and return the maximum count found.





---

Code Implementation:

from collections import defaultdict
from math import gcd

def maxPoints(points):
    if len(points) <= 2:
        return len(points)

    def get_slope(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:  # Vertical line
            return (0, 1)
        if dy == 0:  # Horizontal line
            return (1, 0)
        d = gcd(dx, dy)
        return (dy // d, dx // d)

    max_points = 0

    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicate = 0
        for j in range(len(points)):
            if i == j:
                continue
            if points[i] == points[j]:
                duplicate += 1
            else:
                slope = get_slope(points[i][0], points[i][1], points[j][0], points[j][1])
                slopes[slope] += 1

        current_max = max(slopes.values(), default=0)
        max_points = max(max_points, current_max + duplicate + 1)

    return max_points


---

Explanation of the Code:

1. Edge Case:

If there are 2 or fewer points, all points lie on the same line, so return the total number of points.



2. Slope Calculation:

The slope between two points is calculated and represented as a fraction in reduced form using the GCD.

Vertical lines are represented as (0, 1), and horizontal lines as (1, 0).



3. Hashmap:

Use a hashmap to store the count of points for each unique slope relative to the reference point.



4. Duplicate Points:

Count duplicate points (points with the same coordinates as the reference point) and include them in the result.



5. Maximum Count:

For each reference point, compute the maximum count of points on a line (including duplicates) and update the global maximum.





---

Complexity Analysis:

Time Complexity: 

For each point, we compute slopes for all other points, resulting in  complexity.


Space Complexity: 

The hashmap for storing slopes has a size proportional to the number of points.




---

Examples:

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Explanation: All three points lie on the line .

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation: The maximum number of points on the same line is 4, on the line passing through  and .


---

This approach efficiently calculates the maximum number of points on a single line and handles edge cases like duplicate points and vertical/horizontal lines.



Solution Explanation: Maximum Points on a Line

The goal is to find the maximum number of points that lie on the same straight line from a given list of points in a 2D plane.


---

Key Idea

To solve this problem:

1. Represent each line uniquely using its slope and y-intercept (or handle vertical/horizontal lines separately).


2. Group all points that lie on the same line.


3. Find the maximum number of points in any such group.




---

Algorithm

1. Handle Edge Case

if len(points) == 1:
    return 1

If there's only one point in the input, the result is 1 because a single point always lies on its own line.



---

2. Dictionary to Group Points by Line

lines = defaultdict(lambda: set())

We use a dictionary called lines:

The key is a tuple representing a line. A line is defined either by its slope and y-intercept, or by special values for vertical and horizontal lines.

The value is a set of indices of points that lie on this line. A set ensures no duplicate points are added.




---

3. Iterate Over All Pairs of Points

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x0, y0 = points[i]
        x1, y1 = points[j]
        line = find_Line(x0, y0, x1, y1)
        lines[line].add(i)
        lines[line].add(j)

We iterate through all pairs of points:

For every pair of points  and , calculate the unique representation of the line passing through them using a helper function find_Line.

Add the indices i and j of the points to the set for that line in lines.




---

4. Unique Line Representation

def find_Line(x0, y0, x1, y1):
    if y0 == y1:  # Horizontal line
        return 0, y0
    if x0 == x1:  # Vertical line
        return x0, None
    else:  # General case: calculate slope and intercept
        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        return slope, intercept

Horizontal Lines: If , the line is horizontal. Its key is (0, y0) (constant y-coordinate).

Vertical Lines: If , the line is vertical. Its key is (x0, None) (constant x-coordinate).

General Lines: For all other cases:

Compute the slope: .

Compute the intercept: .

The line's key is the tuple (slope, intercept).



This ensures each line is uniquely identified.


---

5. Find Maximum Points on a Line

return max([len(lines[line]) for line in lines])

After processing all pairs of points:

For each line in the lines dictionary, count the number of unique points (size of the set).

Return the maximum size across all lines.




---

How It Works

Example 1: Input

points = [[1, 1], [2, 2], [3, 3]]

Steps:

1. Initialize lines as an empty dictionary.


2. Iterate through all pairs of points:

For points  and :

Slope = , Intercept = , Line key = (1, 0).

Add indices 0 and 1 to lines[(1, 0)].


For points  and :

Slope = , Intercept = , Line key = (1, 0).

Add index 2 to lines[(1, 0)].


For points  and :

Slope = , Intercept = , Line key = (1, 0).

Indices 1 and 2 are already in lines[(1, 0)].





Resulting lines dictionary:

lines = {
    (1, 0): {0, 1, 2}  # All three points lie on the same line
}

3. The largest set in lines has size 3.



Output:

3


---

Complexity Analysis

Time Complexity

Outer loop:  (iterates through each point).

Inner loop:  (iterates through all other points for each point).

For each pair, finding a line takes .

Total time complexity: , where  is the number of points.


Space Complexity

The dictionary lines can store up to  lines in the worst case.

Each line's set can store  indices.

Total space complexity: .



---

Edge Cases

1. Single Point: Return 1.


2. All Points on One Line: The algorithm identifies the single line with all points.


3. No Points: If the input is empty, return 0 (though this case may not arise due to constraints).




---

Code

from collections import defaultdict

def max_points(points):
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

def find_Line(x0, y0, x1, y1):
    if y0 == y1:  # Horizontal line
        return 0, y0
    if x0 == x1:  # Vertical line
        return x0, None
    else:  # General line (slope-intercept form)
        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        return slope, intercept


---

Example 2: Input

points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

Output:

4

