class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for current_str in strs:
            alpthabet_list = [0] * 26
            for char in current_str:
                alpthabet_list[alphabet.find(char)] += 1
            alphabet_key = tuple(alpthabet_list)
            if alphabet_key not in result_dict.keys():
                result_dict[alphabet_key] = [current_str]
            else:
                result_dict[alphabet_key].append(current_str)
        #print(result_dict)
        return list(result_dict.values())