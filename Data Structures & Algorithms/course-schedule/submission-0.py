class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        non_blocking = []
        requires = {}
        blocks = {}

        for course, prereq in prerequisites:
            # build requires
            if course in requires:
                requires[course].add(prereq)
            else:
                requires[course] = set([prereq])
            # build blocks relationship
            if prereq in blocks:
                blocks[prereq].add(course)
            else:
                blocks[prereq] = set([course])
        
        # build first non_blocking courses
        for course in blocks:
            if course not in requires:
                non_blocking.append(course)
        
        # take courses
        while non_blocking:
            curr = non_blocking.pop()
            for blocked_course in blocks.get(curr, []):
                requires[blocked_course].remove(curr)
                if len(requires[blocked_course]) == 0:
                    del requires[blocked_course]
                    non_blocking.append(blocked_course)

        if requires:
            return False

        return True