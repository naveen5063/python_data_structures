import json
from collections import OrderedDict


class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def groupAnagrams(self, strs):
        global_hash_map = {}
        for str in strs:
            hash_map = {}
            sorted_str = ''.join(sorted(str))
            for i in sorted_str:
                if i in hash_map:
                    hash_map[i] = hash_map[i] + 1
                else:
                    hash_map[i] = 1
            result = json.dumps(hash_map)
            if result in global_hash_map:
                global_hash_map[result].append(str)
            else:
                global_hash_map[result] = [str]
        print("global_hash_map", global_hash_map)
        res = list(global_hash_map.values())
        return res




strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
s = Solution()
print(s.groupAnagrams(strs))