class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        word = bin(n)[2:]
        print(word)
        for i in range(1,len(word)):
            if word[i] == word[i -1]:
                return False
        return True