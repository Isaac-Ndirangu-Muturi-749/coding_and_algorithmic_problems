class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        # Start DFS from room 0
        dfs(0)
        return len(visited) == n
