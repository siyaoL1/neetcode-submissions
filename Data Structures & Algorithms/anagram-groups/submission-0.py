class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_lists = [tuple(sorted(s)) for s in strs]
        # print(str_lists)
        hash_table = {}
        for i in range(len(str_lists)):
            hash_table[str_lists[i]] = hash_table.get(str_lists[i], []) + [strs[i]]

        
        return [value for (key, value) in hash_table.items()]
        # or just list(hash_table.values())