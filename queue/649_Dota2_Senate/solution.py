from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant = deque()
        dire = deque()

        # Initialize the queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)
        # Simulate the rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            # The senator with the smaller index bans the other
            if r < d:
                radiant.append(r + n)  # Radiant senator goes to the back
            else:
                dire.append(d + n)  # Dire senator goes to the back

        # Determine the winner
        return "Radiant" if radiant else "Dire"
