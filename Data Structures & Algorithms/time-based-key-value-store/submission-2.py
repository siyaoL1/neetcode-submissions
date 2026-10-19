class TimeMap:
    # Each key will store the history of the value with timestamp
    # get will use bst to find the position to s get

    def __init__(self):
        self.kv = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        values = self.kv[key]
        left, right = 0, len(values) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result