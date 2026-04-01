class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        while num > 0:
            if num // 1000 > 0:
                s = s + ("M" * (num // 1000))
                num = num % 1000
            elif num // 500 > 0:
                if num // 100 == 9:
                    s = s + "CM"
                    num = num % 900
                else:
                    s = s + ("D" * (num//500))
                    num = num % 500 
            elif num // 100 > 0:
                if num // 100 == 4:
                    s = s + "CD"
                    num = num % 400
                else: 
                    s = s + ("C" * (num//100))
                    num = num % 100
            elif num // 50 > 0:
                if num >= 90:
                    s = s + "XC"
                    num = num % 90
                else:
                    s = s + ("L" * (num//50))
                    num = num % 50
            elif num // 10 > 0:
                if num // 10 == 4:
                    s = s + "XL"
                    num = num % 40
                else: 
                    s = s + ("X" * (num//10))
                    num = num % 10
            elif num // 5 > 0:
                if num == 9:
                    s = s + "IX"
                    num = 0
                else:
                    s = s + ("V" * (num//5))
                    num = num % 5
            elif num // 1 > 0:
                if num == 4:
                    s = s + "IV"
                else:
                    s = s + ("I" * (num//1))
                num = 0
        
        return s
            