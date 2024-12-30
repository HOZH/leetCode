

class Solution:
    def addDigits(self, n: int) -> int:
        n_str = str(n)
        while len(n_str) > 1:
            temp = 0
            for i in n_str:
                temp += int(i)
            n_str = str(temp)

        return int(n_str)



class Solution:
    def addDigits(self, num: int) -> int: #10
        return 1 + (num - 1) % 9 if num else 0

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        
        str_num = str(num)
        count = 0
        for i in str_num:
            count += int(i)
        
        return self.addDigits(count)
    

class Solution:
    def __init__(self):
        self.allowed_primes = set([2, 3, 5])

    def isUgly(self, n: int) -> bool: # 14

        if n < 1:
            return False
        if n == 1:
            return True

        if n in self.allowed_primes:
            return True

        failure_count = 0
        for i in self.allowed_primes: # 2 -> 14 // 2 -> 7 -> isUgly(7) 
            if n % i == 0 and self.isUgly(n // i): # 14/ 3  , 14/ 5 -> 2
                return True

            failure_count += 1
            if failure_count == 3:
                return False
  


 def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        can_divide_by_two = False
        can_divide_by_three = False
        can_divide_by_five = False

        try:
            two_divide = n / 2 # 14 / 2 -> 7.0
            can_divide_by_two = True
        except Exception:
            can_divide_by_two = False

        try:
            three_divide = n / 3 # 14 / 3 -> 4.3
            can_divide_by_three = True
        except Exception:
            can_divide_by_three = False
        
        try:
            five_divide = n / 5 # 14 / 5 -> 2....
            can_divide_by_five = True
        except Exception:
            can_divide_by_five = False

        return can_divide_by_two and can_divide_by_three and can_divide_by_five

from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num).is_integer()