class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = Counter(s)
        stack = []
        dic2 = defaultdict(int)
        for c in s:
            dic[c] -= 1
            if dic[c] == 0:
                del dic[c]
            if c not in dic2:
                while stack and c <= stack[-1] and stack[-1] in dic:
                    lett = stack.pop()
                    dic2[lett] -= 1
                    if dic2[lett] == 0:
                        del dic2[lett]
                stack.append(c)
                dic2[c] += 1
        #print(dic2)
        return "".join(stack)