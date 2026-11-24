class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict_s = [0] * 26
        freq_dict_t = [0] * 26
        lenght = len(s)
        if lenght != len(t):
            return False
        for current in range(lenght):
            freq_dict_s[ord(s[current]) - ord('a')] += 1
            freq_dict_t[ord(t[current]) - ord('a')] += 1
        if freq_dict_s != freq_dict_t:
            return False
        return True