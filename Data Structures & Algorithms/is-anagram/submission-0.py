class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.buildDict(s)
        t_dict = self.buildDict(t)
        if len(s_dict) != len(t_dict):
            return False
        for l in s_dict:
            if l not in t_dict or s_dict[l] != t_dict[l]:
                return False
        return True

        
    def buildDict(self, s):
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        return s_dict

        