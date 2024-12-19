class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stack to store indices of temperatures

        for i in range(n):
            # While the current temperature is warmer than the temperature at stack[-1]
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            # Push the current index onto the stack
            stack.append(i)

        return answer
