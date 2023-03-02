class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isdigit():
            return ""
        stack = []
        for i in range(len(s)):
            if s[i].isdigit() and stack and stack[-1].isdigit():
                a = stack.pop()
                stack.append(a+s[i])
            elif s[i] != "]":
                stack.append(s[i])
            else:
                #print(stack)
                new_word = []
                while stack[-1] != "[":
                    new_word.append(stack.pop())
                stack.pop()
                stack += int(stack.pop())*list(reversed(new_word))
        return "".join(stack)