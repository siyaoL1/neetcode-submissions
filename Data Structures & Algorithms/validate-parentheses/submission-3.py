class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {')': '(', '}': '{', ']': '['}
        opens = set(pair_map.values())
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) < 1 or stack.pop() != pair_map[c]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
            