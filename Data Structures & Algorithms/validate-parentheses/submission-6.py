class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {')':'(', '}':'{', ']':'['}
        stack = []

        for bracket in s:
            if bracket in brackets_map:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if brackets_map[bracket] != last:
                    return False 

                continue

            stack.append(bracket)

        return len(stack) == 0                

            

