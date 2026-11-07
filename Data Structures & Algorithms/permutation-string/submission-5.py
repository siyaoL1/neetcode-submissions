class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        diff = {}
        def adjust(char, delta):
            count = diff.get(char, 0) + delta
            if count == 0:
                del diff[char]
            else:
                diff[char] = count

        for c in s1:
            adjust(c, -1)
        for i in range(len(s1)):
            adjust(s2[i], 1)
        if not diff:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            adjust(s2[right], 1)
            adjust(s2[left], -1)
           
            if not diff:
                return True
            left += 1
            right += 1
            
        return False


