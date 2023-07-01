class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def findGraph():
            graph = [[] for _ in range(numCourses)]
            for a, b in prerequisites:
                graph[a].append(b)
            return graph

        def hasCycle(i):
            if seen[i] == 1:
                return False
            if seen[i] == -1:
                return True
            seen[i] = -1

            for each in graph[i]:
                if hasCycle(each):
                    return True
            seen[i] = 1
            return False

        graph = findGraph()

        seen = [0] * numCourses
        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True

            
