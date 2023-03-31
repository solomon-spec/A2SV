class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        rem = 0
        new = []
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0: cur = int(a[i]) + int(b[j]) + rem
            elif i >= 0: cur = int(a[i]) + rem
            else: cur = int(b[j]) + rem
            if cur == 3:
                rem = 1
                new.append("1")
            elif cur == 2:
                rem = 1
                new.append("0")
            elif cur == 1:
                rem = 0
                new.append("1")
            else:
                rem = 0
                new.append("0")
            i -= 1
            j -= 1
        if rem == 1 : new.append("1")
        return "".join(reversed(new))
        