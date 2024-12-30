This problem can be solved using a stack. The stack helps track the asteroids that are moving to the right (positive) and will collide with incoming left-moving (negative) asteroids.

Algorithm:

1. Use a stack to simulate the process:

Push positive asteroids (moving right) onto the stack.

For a negative asteroid (moving left), check the stack:

If the stack is empty or the top of the stack is also negative, push the asteroid onto the stack.

If the top of the stack is positive, simulate a collision:

If the absolute value of the negative asteroid is smaller, pop the positive asteroid from the stack.

If the absolute value of the negative asteroid is larger, keep the negative asteroid and continue checking.

If the sizes are equal, both asteroids explode (remove the positive asteroid and skip the negative asteroid).





2. At the end, the stack will contain the remaining asteroids.




---

Python Implementation:

def asteroidCollision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            # Handle collision
            if abs(asteroid) > stack[-1]:
                stack.pop()  # Remove the smaller positive asteroid
                continue
            elif abs(asteroid) == stack[-1]:
                stack.pop()  # Both explode
            break
        else:
            stack.append(asteroid)
    
    return stack


---

Example Walkthrough:

Example 1:

asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))  # Output: [5, 10]

Push 5 → [5]

Push 10 → [5, 10]

Collision: 10 (stack top) vs -5 → -5 explodes. Result: [5, 10].



---

Example 2:

asteroids = [8, -8]
print(asteroidCollision(asteroids))  # Output: []

Push 8 → [8]

Collision: 8 vs -8 → Both explode. Result: [].



---

Example 3:

asteroids = [10, 2, -5]
print(asteroidCollision(asteroids))  # Output: [10]

Push 10 → [10]

Push 2 → [10, 2]

Collision: 2 vs -5 → 2 explodes. Stack: [10]

Collision: 10 vs -5 → -5 explodes. Result: [10].



---

Complexity Analysis:

1. Time Complexity: , where  is the length of the asteroids array. Each asteroid is pushed and popped from the stack at most once.


2. Space Complexity: , for the stack in the worst case when no collisions occur.



This implementation efficiently handles the simulation of asteroid collisions.

