class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        current = 0
        seen = set()
        while temp != 1:
            seen.add(temp)
            current = 0
            for i in str(temp):   # string = 'abs', [*string]=> ['a','b','c'] [string] => ['abc']
                current += int(i)**2
            temp = int(current)
            if temp in seen:
                return False
        return True


    def isHappy(self, n: int) -> bool:
        visited = set()
        current = n
        if n == 1:
            return True
        while current != 1:
            current = sum([int(digit) ** 2 for digit in str(current)])
            if current == 1:
                return True
            if current in visited:
                return False
            else:
                visited.add(current)
            




class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        ceiling = (2**31) - 1
        if n == 2 or n == 3 or n == ceiling: # n 2**2 = 4, n = 3, 9, 81, 65, 36 + 25, 61, 37, 
            return False
        
        str_num = str(n) # n = 4, 16, 37, 58, 25 + 64 = 89, .. 
        total = 0
        for char in str_num:
            num = int(char)
            total = total + (num * num)
        
        output = self.isHappy(total)
        return output


        ###
     def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

