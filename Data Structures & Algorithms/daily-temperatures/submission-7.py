class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                colder_temp, colder_index = stack.pop()
                result[colder_index] = i - colder_index
            stack.append((temp, i))
        
        return result

                 

