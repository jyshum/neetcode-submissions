class Solution:
    def isValid(self, s: str) -> bool:
        syntax = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        # as we loop through each char in the string, check in syntax if the char 
        for char in s:
            if char in syntax:
                # open bracket
                stack.append(char)
            else:
                # closed bracket
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if syntax[top] != char:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
