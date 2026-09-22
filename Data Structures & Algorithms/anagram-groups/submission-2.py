from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for current_str in strs:
            alpthabet_list = [0] * 26
            for char in current_str:
                alpthabet_list[ord(char) - ord('a')] += 1
            alphabet_key = tuple(alpthabet_list)
            result_dict[alphabet_key].append(current_str)
        #print(result_dict)
        return list(result_dict.values())