class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'] 
        } 
        prev_ans = ['']
        for dig in digits:
            new_ans = []
            for i in prev_ans:
                for l in dic[int(dig)]:
                    new_ans.append(i+l)
            prev_ans = new_ans
        return prev_ans