class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "[{(":
                stack.append(char)
            elif (char in "]})"):
                if not stack:
                    return False
                if (char == ")" and stack[-1] == "(") or \
                (char == "]" and stack[-1] == "[") or \
                (char == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            else:
                continue
        
        if len(stack) == 0:
            return True
        else:
            return False