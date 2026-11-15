class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_order = []
        letter_index = {}
        for i in range(len(s)):
            c = s[i]
            if c not in letter_index:
                letter_index[c] = [i, i]
                letter_order.append(c)
            else:
                letter_index[c][1] = i

        # Merge overlapping ranges
        result = []
        prev_s = 0
        prev_e = 0
        for c in letter_order:
            s, e = letter_index[c]
            if s > prev_e:
                result.append(prev_e - prev_s + 1)
                prev_s = s
            prev_e = max(e, prev_e)
        result.append(prev_e - prev_s + 1)
        
        return result
        