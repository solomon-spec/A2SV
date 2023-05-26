word1 = input()
word2 = input()
word3 = word1 + word2
word4 = input()
if sorted(list(word3)) == sorted(list(word4)): print("YES")
else: print("NO")