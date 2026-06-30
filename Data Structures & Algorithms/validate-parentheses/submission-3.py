class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        if len(s) %2 != 0:
            return False

        for c in s:
            if c in brackets:
                if not stack:
                    return False 
                c_ = stack.pop()
                if c_ != brackets[c]:
                    return False

            else:
                stack.append(c)

        return len(stack) == 0
        