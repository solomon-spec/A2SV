class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        crr, stack = 0, []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                while stack[-1] != '(':
                    crr += stack[-1]
                    stack.pop()
                stack[-1] = crr * 2 if crr else 1
                crr = 0
        return sum(stack)
                