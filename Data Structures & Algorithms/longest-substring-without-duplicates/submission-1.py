class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0 
        right = 0
        temp_set = set(s[0])
        max_lenght = 1
        while right < len(s) - 1:
            right += 1
            while s[right] in temp_set:
                temp_set.remove(s[left])
                left += 1
            else:
                temp_set.add(s[right])
                max_lenght = max(max_lenght, len(temp_set))
        return max_lenght
        