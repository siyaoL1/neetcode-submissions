class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gains = []
        for i in range(len(gas)):
            gains.append(gas[i] - cost[i])

        if sum(gains) < 0:
            return -1
        
        remaining_gas = 0
        start_index = 0
        
        for curr_index, gain in enumerate(gains):
            remaining_gas += gain
            if remaining_gas < 0:
                remaining_gas = 0
                start_index = curr_index + 1
        
        return start_index
