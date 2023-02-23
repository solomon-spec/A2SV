class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix= [0]*(len(s) + 1)
        for l,r,num in shifts:
            if num == 0:
                prefix[l] -= 1
                prefix[r + 1] += 1
            else:
                prefix[l] += 1
                prefix[r + 1] -= 1
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        new = []
        for i in range(len(s)):
            shift = prefix[i] % 26
            print(shift)
            new.append(chr((ord(s[i]) - 97 + shift)%26 + 97))
        return "".join(new)