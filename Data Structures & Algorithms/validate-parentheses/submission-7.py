class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {')':'(', '}':'{', ']':'['}
        li = [')', ']', '}']
        stack = []

        for bracket in s:
            if bracket in li:
                if len(stack) == 0:
                    return False
                if brackets_map[bracket] != stack.pop():
                    return False 
                continue

            stack.append(bracket)

        return len(stack) == 0                

            

