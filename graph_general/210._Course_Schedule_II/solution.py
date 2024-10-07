class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Step 1: Initialize the graph and the in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Step 2: Build the graph and populate the in-degree of each node
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 3: Initialize the queue with all courses that have no prerequisites (in-degree of 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        # Step 4: Process the queue (BFS)
        while queue:
            course = queue.popleft()
            result.append(course)

            # Reduce the in-degree of all the neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If we were able to process all courses, return the result, otherwise return []
        if len(result) == numCourses:
            return result
        else:
            return []
