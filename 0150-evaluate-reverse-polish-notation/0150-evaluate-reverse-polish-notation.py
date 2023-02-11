class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        arr = []
        dic = {
            "*": lambda a,b : int(a * b),
            "/": lambda a,b : int(a / b) if a*b > 0 else - int(-a/b),
            "-": lambda a,b : int(a - b),
            "+": lambda a,b : int(a + b)
        }
        for num in tokens:
            if num not in dic:
                arr.append(int(num))
            else:
                a = arr.pop()
                b = arr.pop()
                arr.append(dic[num](b,a))
        return arr[0]