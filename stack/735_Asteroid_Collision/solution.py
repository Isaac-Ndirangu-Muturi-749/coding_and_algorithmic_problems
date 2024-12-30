class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

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
