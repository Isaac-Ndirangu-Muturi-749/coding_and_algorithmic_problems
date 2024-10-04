from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create an adjacency list for the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Step 2: Create a state array to track the visiting status of each node
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        # Step 3: Helper function to perform DFS
        def dfs(course):
            if state[course] == 1:  # Cycle detected (visiting again)
                return False
            if state[course] == 2:  # Already visited, no cycle from this node
                return True

            # Mark the node as visiting
            state[course] = 1

            # Visit all the neighbors (i.e., courses that depend on the current course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # After visiting all neighbors, mark the node as visited
            state[course] = 2
            return True

        # Step 4: Apply DFS to every course
        for course in range(numCourses):
            if state[course] == 0:  # Only start DFS for unvisited nodes
                if not dfs(course):
                    return False

        return True
