To calculate how much water can be trapped after raining based on the elevation map, we need to determine the amount of water above each bar by considering the tallest bars to the left and right of the current bar.


---

Key Idea

1. Water Above Each Bar:

The water above the -th bar is determined by the minimum of:

The tallest bar to its left.

The tallest bar to its right.


Subtract the height of the -th bar from this minimum.




\text{Water Above Bar } i = \max(\min(\text{maxLeft}[i], \text{maxRight}[i]) - \text{height}[i], 0)

2. Optimization:

Use two-pointer technique for optimal time and space complexity:

Maintain left and right pointers and iterate toward each other.

Calculate water by dynamically keeping track of max heights.






---

Algorithm

Approach 1: Precompute Left and Right Maximum Heights

1. Compute Left Max:

Create an array maxLeft where  stores the maximum height to the left of  (including ).



2. Compute Right Max:

Create an array maxRight where  stores the maximum height to the right of  (including ).



3. Calculate Water:

For each bar, calculate trapped water as .





---

Approach 2: Two-Pointer Technique (Optimized)

1. Initialize two pointers:

left starting at 0.

right starting at the last index.



2. Maintain two variables:

maxLeft and maxRight to keep track of the tallest bars seen so far on the left and right.



3. Iterate:

If height[left] <= height[right]:

Update maxLeft.

Calculate water above the left bar.

Increment left.


Else:

Update maxRight.

Calculate water above the right bar.

Decrement right.






---

Code Implementation

Approach 1: Precompute Left and Right Maximums

def trap(height):
    if not height:
        return 0
    
    n = len(height)
    maxLeft = [0] * n
    maxRight = [0] * n
    
    # Fill maxLeft
    maxLeft[0] = height[0]
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i-1], height[i])
    
    # Fill maxRight
    maxRight[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        maxRight[i] = max(maxRight[i+1], height[i])
    
    # Calculate trapped water
    water = 0
    for i in range(n):
        water += min(maxLeft[i], maxRight[i]) - height[i]
    
    return water

Approach 2: Two-Pointer Technique (Optimized)

def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    maxLeft, maxRight = 0, 0
    water = 0
    
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                water += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                water += maxRight - height[right]
            right -= 1
    
    return water


---

Example Walkthrough

Example 1:

Input:

height = [0,1,0,2,1,0,1,3,2,1,2,1]

1. Using the two-pointer technique:

Initial state: left = 0, right = 11, maxLeft = 0, maxRight = 0, water = 0.

Process each step by comparing height[left] and height[right].

Final result: water = 6.




Example 2:

Input:

height = [4,2,0,3,2,5]

1. Using the two-pointer technique:

Initial state: left = 0, right = 5, maxLeft = 0, maxRight = 0, water = 0.

Process each step by comparing height[left] and height[right].

Final result: water = 9.





---

Complexity Analysis

Time Complexity:

Precompute Method:  for filling maxLeft, maxRight, and calculating water.

Two-Pointer Method: , as we iterate through the array once.


Space Complexity:

Precompute Method:  for maxLeft and maxRight.

Two-Pointer Method: , as we only use variables.



---

Final Notes

The two-pointer approach is preferred due to its optimal space complexity of , making it suitable for larger input sizes.

