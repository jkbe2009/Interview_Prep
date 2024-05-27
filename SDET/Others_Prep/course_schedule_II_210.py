
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        """
        res = []
        t_d = {}
        d_t = {}
        comp = set()
        not_comp = set(i for i in range(numCourses))
        full_list = [i for i in range(numCourses)]

        if len(prerequisites) == 0:
            return full_list

        for val in prerequisites:
            task = val[0]
            dep = val[1]
            t_d.setdefault(task, []).append(dep)
            d_t.setdefault(dep, []).append(task)
        
        # Handle cyclic dependency
        for t,dl in t_d.items():
            for d in dl:
                if d in t_d and t in t_d[d]: # There is a cycle
                    return []

        # Get sorted dependencies list
        sorted_dep = sorted(d_t.keys())

        # Mark all the tasks without dep as completed
        for task in full_list :
            if task not in t_d:
                if task in not_comp:
                    not_comp.remove(task)
                if task not in comp:
                    res.append(task)
                comp.add(task)

        while not_comp:
            for dep in sorted_dep:
                task_list = d_t[dep]
                for task in task_list:
                    for d in t_d[task]:
                        if d in comp:
                            # Mark that task as completed
                            if task in not_comp:
                                not_comp.remove(task)
                            if task not in comp:
                                res.append(task)
                            comp.add(task)


        return res
        """

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dep = {i : [] for i in range(numCourses)}

        for c,p in prerequisites:
            dep[c].append(p)

        visited = set()
        added = set()
        res = []

        def dfs(course):
            if course in visited:
                return False
            
            if course in added:
                return True
            
            if dep[course] == []:
                added.add(course)
                res.append(course)
                return True
            
            visited.add(course)
            for c in dep[course]:
                if not dfs(c):
                    return False
            
            visited.remove(course)
            added.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res