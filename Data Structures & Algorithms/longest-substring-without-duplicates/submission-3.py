class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0 
        right = 0
        temp_set = set()
        max_lenght = 1
        for right in range(len(s)):
            while s[right] in temp_set:
                temp_set.remove(s[left])
                left += 1
            temp_set.add(s[right])
            max_lenght = max(max_lenght, right - left + 1)
        return max_lenght
        