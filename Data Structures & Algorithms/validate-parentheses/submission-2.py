class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            if char == ")":
                if len(stack) == 0:
                    return True
                if stack.pop() != "(":
                    return False
            if char == "}":
                if len(stack) == 0:
                    return True
                if stack.pop() != "{":
                    return False
            if char == "]":
                if len(stack) == 0:
                    return True
                if stack.pop() != "[":
                    return False
        return True        