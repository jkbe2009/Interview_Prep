
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dep = {i : [] for i in range(numCourses)}

        for c,p in prerequisites:
            dep[c].append(p)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if dep[course] == []:
                return True
            
            visited.add(course)
            for c in dep[course]:
                if not dfs(c):
                    return False
            
            visited.remove(course)
            dep[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True