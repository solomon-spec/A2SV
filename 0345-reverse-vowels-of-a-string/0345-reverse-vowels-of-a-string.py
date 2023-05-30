class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a","e","i","o","u"])
        arr = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                arr.append(i)
        sl = list(s)
        for i in range(len(arr)//2):
            sl[arr[i]],sl[arr[-i-1]] = sl[arr[-i-1]],sl[arr[i]]
        return "".join(sl)