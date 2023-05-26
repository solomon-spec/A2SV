word = list(input())
word2 = input()
word.sort()
i = 0
if word.count("0") < len(word):
    while word[0] == "0":
        if word[i] =="0": i+=1
        else: word[0],word[i] = word[i],word[0]
x = "".join(word)
if x == word2: print("OK")
else: print("WRONG_ANSWER")
