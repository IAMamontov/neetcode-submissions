class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_removed = ("".join(ch for ch in s if ch.isalnum())).lower()
        for i in range(len(s_removed) // 2):
            if s_removed[i] != s_removed[-i - 1]:
                return False
        return True