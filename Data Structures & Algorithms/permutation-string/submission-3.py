class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        diff = {}
        for c in s1:
            if c in diff:
                diff[c] -= 1
            else:
                diff[c] = -1

        for i in range(len(s1)):
            c = s2[i]
            if c in diff:
                diff[c] += 1
                if diff[c] == 0:
                    diff.pop(c)
            else:
                diff[c] = 1
        if not diff:
            return True

        left = 0
        right = len(s1)

        while right< len(s2):
            right_c = s2[right]
            print(f"right_c:{right_c}")
            if right_c in diff:
                diff[right_c] += 1
                if diff[right_c] == 0:
                    diff.pop(right_c)
            else:
                diff[right_c] = 1

            left_c = s2[left]
            print(f"left_c:{left_c}")
            if left_c in diff:
                diff[left_c] -= 1
                if diff[left_c] == 0:
                    diff.pop(left_c)
            else:
                diff[left_c] = -1
            print(diff)
            if not diff:
                return True
            left += 1
            right += 1
            
        
        return False


