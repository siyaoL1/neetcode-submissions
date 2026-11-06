class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependents = {}
        dependencies = {}

        for parent, child in prerequisites:
            curr = dependents.setdefault(child, set())
            curr.add(parent)
            curr = dependencies.setdefault(parent, set())
            curr.add(child)

        # Courses with no prerequisite
        stack = []
        for i in range(numCourses):
            if i not in dependencies:
                stack.append(i)
        
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr)
            for parent in dependents.get(curr, set()):
                dependencies[parent].remove(curr)
                if not dependencies[parent]:
                    dependencies.pop(parent)
                    stack.append(parent)
        if dependencies:
            return []
        
        return result
