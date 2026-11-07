class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]

        pairs.sort()

        count = 0
        prev_time = None
        for i in range(len(pairs) - 1, -1, -1):
            curr_pos, curr_speed = pairs[i]
            curr_time = (target - curr_pos) / curr_speed

            if not prev_time or curr_time > prev_time:
                prev_time = curr_time
                count += 1

        return count