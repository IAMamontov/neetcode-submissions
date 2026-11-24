from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_list = []
        anagrams = defaultdict(list)
        for current_str in strs:
            alphabet_list = [0] * 26
            for current_char in current_str:
                alphabet_list[ord(current_char) - ord('a')] += 1
            alphabet_tuple = tuple(alphabet_list)
            anagrams[alphabet_tuple].append(current_str)
        for k in anagrams:
            result_list.append(anagrams[k])
        return result_list