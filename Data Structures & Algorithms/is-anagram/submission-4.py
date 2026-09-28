class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        
        t_dict = {}
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        
        return s_dict == t_dict