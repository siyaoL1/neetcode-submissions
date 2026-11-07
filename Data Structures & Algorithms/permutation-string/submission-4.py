class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        diff = {}
        def remove(c):
            if c in diff:
                diff[c] -= 1
                if diff[c] == 0:
                    diff.pop(c)
            else:
                diff[c] = -1
        
        def add(c):
            if c in diff:
                diff[c] += 1
                if diff[c] == 0:
                    diff.pop(c)
            else:
                diff[c] = 1

        for c in s1:
            remove(c)
        for i in range(len(s1)):
            add(s2[i])
        if not diff:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            add(s2[right])
            remove(s2[left])
           
            if not diff:
                return True
            left += 1
            right += 1
            
        return False


