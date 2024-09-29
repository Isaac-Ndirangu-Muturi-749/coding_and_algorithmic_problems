class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        # Sort the balloons by their xend values (end of the diameter)
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        last_arrow_position = points[0][1]  # Position of the first arrow at the end of the first balloon

        # Iterate through the sorted points
        for xstart, xend in points:
            # If the current balloon's start is greater than the last arrow's position, shoot a new arrow
            if xstart > last_arrow_position:
                arrows += 1
                last_arrow_position = xend  # Update the position of the last arrow to the current balloon's end

        return arrows
