class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        freq_dict_s, freq_dict_t = {}, {}
        for i in range(len(s)):
            freq_dict_s[s[i]] = freq_dict_s.get(s[i], 0) + 1
            freq_dict_t[t[i]] = freq_dict_t.get(t[i], 0) + 1
        if freq_dict_s != freq_dict_t:
            return False
        return True
        