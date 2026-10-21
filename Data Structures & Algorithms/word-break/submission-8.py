class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = {0}
        stack = [0]

        while stack:
            start = stack.pop()
            for word in wordDict:
                if s.startswith(word, start):
                    next_start = start + len(word)
                    if next_start == len(s):
                        return True
                    if next_start not in visited:
                        visited.add(next_start)
                        stack.append(next_start)
        
        return False