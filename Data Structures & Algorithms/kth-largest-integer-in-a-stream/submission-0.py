class KthLargest:

    # I'm thinking about building a binary search tree with list as the type, child = curr_index * 2 + 1 and + 2
    # but now I think heap will also work
    # where we keep two heaps, one keeps to be k size max, and the second one for the rest
    # I will try both
    def __init__(self, k: int, nums: List[int]):
        # Solution 1
        self.bst = []
        self.k = k
        for num in nums:
            self.add(num)

    def _insert(self, val: int) -> None:
        index = 0

        while index < len(self.bst) and self.bst[index] is not None:
            if val < self.bst[index]:
                index = 2 * index + 1
            else:
                index = 2 * index + 2

        while len(self.bst) <= index:
            self.bst.append(None)

        self.bst[index] = val
        

    def add(self, val: int) -> int:
        self._insert(val)
        visited = 0
        result = None

        def dfs(index):
            nonlocal visited, result

            if (
                index >= len(self.bst)
                or self.bst[index] is None
                or visited >= self.k
            ):
                return
            
            dfs(2 * index + 2)  # Larger values first.

            if visited >= self.k:
                return

            visited += 1
            if visited == self.k:
                result = self.bst[index]
                return

            dfs(2 * index + 1)

        dfs(0)
        return result
