class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We have a list of courses
        # To finish all of them we should start from lower leveled courses, i.e. courses with no dependencies, and cross out dependencies
        # Continue taking courses with no dependencies until we can't
        # If we still have courses with dependencies left, then false
        

        # Preprocess prerequisites
        requires = {}
        blocks = {}

        for upper, lower in prerequisites:
            if upper in requires:
                requires[upper].add(lower)
            else:
                requires[upper] = set([lower])

            if lower in blocks:
                blocks[lower].add(upper)
            else:
                blocks[lower] = set([upper])
        
        # get initial course that has no dependencies
        non_blocking = []
        for course in blocks:
            if course not in requires:
                non_blocking.append(course)
        
        # keep processing until we processed all possible dependencies
        while non_blocking:
            curr = non_blocking.pop()
            unblocks = blocks.get(curr, set())
            for course in unblocks:
                requires[course].remove(curr)
                if not requires[course]:
                    del requires[course]
                    non_blocking.append(course)
        
        if requires:
            return False
        
        return True

