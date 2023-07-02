class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        edgesTo = [[] for _ in range(numCourses)]
        incomingEdges = [0] * numCourses
        for a, b in prerequisites:
           edgesTo[b].append(a)
           incomingEdges[a] += 1

        q = []
        for index in range(numCourses):
            if incomingEdges[index] == 0:
                q.append(index)

        ordering = []
        count = 0
        while(q):
            count += 1
            current = q.pop()
            ordering.append(current)
            for each in edgesTo[current]:
                incomingEdges[each] -= 1
                if incomingEdges[each] == 0:
                    q.append(each)

        if count == numCourses:
            return ordering
        else:
            return []



        