class Solution:
    def candy(self, ratings):
        xxx = 0
        prev_inc = False
        prev_prev = False
        length = len(ratings)
        if length <= 1:
            return 1
        inc = True if ratings[0] < ratings[1] else False
        i = 0
        answer = []
        valley = 0
        ans = 0
        while i < length - 1:
            leng = 1
            if inc == True:
                while i+1 < length and ratings[i] < ratings[i + 1]:
                    leng += 1
                    i += 1
                
                if i + 1 < length:
                    if ratings[i] == ratings[i + 1]:
                        i += 1
                    if i - 1 >= 0 and ratings[i -1] < ratings[i] > ratings[i +1]:
                        prev_inc  = True
                    else:
                        prev_inc = False
                 
                answer.append(leng)
                inc = False
            else:
                while i+1 < length and ratings[i] > ratings[i + 1]:
                    leng += 1
                    i += 1
                if i + 1 < length and ratings[i] == ratings[i + 1]:
                    i += 1
                if i + 1 < length and i - 1 > 0 and ratings[i] < ratings[i + 1] and ratings[i] == ratings[i - 1] > ratings[i - 2]  :
                        leng -= 1
                if i + 1 < length and ratings[i] < ratings[i + 1]:
                    if i - 1 >= 0 and ratings[i -1] > ratings[i]:
                        valley  += 1
                    inc = True
                """if i - 1 > 0 and i + 1 < length:
                    if (ratings[i - 1] == ratings[i] < ratings[i + 1]) and not prev_prev:
                        xxx += 1"""
                answer.append(leng)
                prev_inc = False
            if len(answer) > 1 and prev_prev == True:
                if answer[-1] > answer[-2]:
                    answer[-2] -= 1
                else:
                    answer[-1] -= 1
            prev_prev = prev_inc
           
        if length > 1 and ratings[-1] == ratings[-2]:
                answer.append(1)   
        for i in answer:
            ans += (i**2 + i)/2
        print(answer,valley,xxx)
        return int(ans -valley - xxx)