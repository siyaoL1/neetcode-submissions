class Solution:
    def isAnagram_dict(self, s: str, t: str) -> bool:
        s_dict = self.buildDict(s)
        t_dict = self.buildDict(t)
        if len(s_dict) != len(t_dict):
            return False
        for l in s_dict:
            if l not in t_dict or s_dict[l] != t_dict[l]:
                return False
        return True
        # from hint: python dictionary can be compared directly so no need to do loop
        # also from hint: Counter(s) == Counter(t) does the thing directly holy shit.

        
    def buildDict(self, s):
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        return s_dict

    # O(nlog(n)), O(n)
    def isAnagram_sort(self, s: str, t: str) -> bool:
        s_list = list(s) # O(s), O(|s|)
        t_list = list(t) # O(t), O(|t|)

        s_list.sort() # O(nlog(s))
        t_list.sort() # O(nlog(t))

        return s_list == t_list # O(min(s, t))
        # from hint: return sorted(s) == sorted(t) also works

    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for l in s:
            # print(l, ord(l), ord('a'), ord(l) - ord('a'), len(freq))
            freq[ord(l) - ord('a')] += 1
            # print(freq)
        for l in t:
            freq[ord(l) - ord('a')] -= 1
            # print(freq)
        for l in freq:
            if l != 0:
                return False
        return True



        