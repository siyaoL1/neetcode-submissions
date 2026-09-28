class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {')':'(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in brackets_map:
                if not stack:
                    return False
                if stack.pop() != brackets_map[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True
            