class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        freq_dict_s, freq_dict_t = {}, {}
        for char in set(s):
            freq_dict_s[char] = freq_dict_s.get(char, 0) + 1
            freq_dict_t[char] = freq_dict_t.get(char, 0) + 1
        if freq_dict_s != freq_dict_t:
            return False
        return True
        