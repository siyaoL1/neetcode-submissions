class Solution:
    #Total Space: O(nk)
    #Total Time: O(nklog(k)) + O(nk + n^2)
    def groupAnagrams_org(self, strs: List[str]) -> List[List[str]]:
        # Space: O(nk) Time: nklog(k)
        str_lists = [tuple(sorted(s)) for s in strs]
        # Space: O(nk)
        hash_table = {}
        # Time: O(n) *(O(1) * O(k) + O(1) + O(n))
        for i in range(len(str_lists)):
            hash_table[str_lists[i]] = hash_table.get(str_lists[i], []) + [strs[i]]

        # Time: O(min(k, n))
        return [value for (key, value) in hash_table.items()]
        # or just list(hash_table.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Space: O(nk) Time: nklog(k)
        str_lists = [tuple(sorted(s)) for s in strs]
        # Space: O(nk)
        hash_table = {}
        # Time: O(n) *(O(1) * O(k) + O(1) + O(n))
        for i in range(len(str_lists)):
            if str_lists[i] in hash_table:
                hash_table[str_lists[i]].append(strs[i])
            else:
                hash_table[str_lists[i]] = [strs[i]]

        # Time: O(min(k, n))
        return [value for (key, value) in hash_table.items()]
        # or just list(hash_table.values())