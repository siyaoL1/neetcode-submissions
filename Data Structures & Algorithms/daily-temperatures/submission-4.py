import heapq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for index in range(len(temperatures)):
            curr = temperatures[index]
            while stack:
                if stack[-1][0] < curr:
                    cold_index = stack.pop()[1]
                    result[cold_index] = index - cold_index
                else:
                    break
            
            stack.append((curr, index))
        return result
