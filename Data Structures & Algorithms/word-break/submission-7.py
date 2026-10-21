class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = {0}
        pending_suffix_index = [0]

        while pending_suffix_index:
            curr_index = pending_suffix_index.pop()
            for word in wordDict:
                word_len = len(word)
                if s.startswith(word, curr_index):
                    remaining_index = curr_index + word_len
                    if remaining_index == len(s):
                        return True
                    if remaining_index not in visited:
                        visited.add(remaining_index)
                        pending_suffix_index.append(remaining_index)
        
        return False