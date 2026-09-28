class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            k = tuple(freq)
            if k in anagram_dict:
                anagram_dict[k].append(word)
            else:
                anagram_dict[k] = [word]

        return list(anagram_dict.values())
        