from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize an empty queue
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the new request timestamp to the queue
        self.requests.append(t)

        # Remove timestamps outside the valid range
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # The size of the queue is the number of valid requests
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
