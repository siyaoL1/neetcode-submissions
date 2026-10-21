class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = {s}
        pending = [s]

        while pending:
            curr_string = pending.pop()
            curr_string_len = len(curr_string)
            for word in wordDict:
                word_len = len(word)
                if word_len <= curr_string_len and curr_string[:word_len] == word:
                    remaining_string = curr_string[word_len:]
                    if not remaining_string:
                        return True
                    if remaining_string not in visited:
                        visited.add(remaining_string)
                        pending.append(remaining_string)
        
        return False