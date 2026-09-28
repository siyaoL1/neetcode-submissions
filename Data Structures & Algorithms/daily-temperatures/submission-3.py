import heapq

class Solution:
    def dailyTemperaturesBruteForce(self, temperatures: List[int]) -> List[int]:
        # Brute force
        length = len(temperatures)
        result = []
        for i in range(length):
            days = 0
            for j in range(i + 1, length):
                if temperatures[j] > temperatures[i]:
                    days = j - i
                    break
            result.append(days)
        
        return result
            
    def dailyTemperaturesHeap(self, temperatures: List[int]) -> List[int]:
        # Note that I had to look up heap syntex
        result = [0] * len(temperatures)
        min_heap = []
        for i in range(len(temperatures)):
            while len(min_heap) > 0 and min_heap[0][0] < temperatures[i]:
                lower_temp, lower_index = heapq.heappop(min_heap)
                result[lower_index] = i - lower_index
            heapq.heappush(min_heap, (temperatures[i], i))

        return result
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                _, lower_index = stack.pop()
                result[lower_index] = i - lower_index
            stack.append((temperatures[i], i))

        return result
