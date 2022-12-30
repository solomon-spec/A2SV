class Solution(object):
    def multiply(self, num1, num2):
        
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        number1 = 0
        number2  = 0
        for number in num1:
            number1 = number1*10 + ord(number)-48
        for number in num2:
            number2 = number2*10 + ord(number)-48
        return (str(number1*number2))           
        