https://leetcode.com/problems/count-and-say/description/



function(3) = 21  ->  2  1 function(2) -> (11) -> 21
 1 2    

 func(1) -> "1"
 func(2) '1' -> "11"
 func(3) "11" -> "21"
 func(4)"2 1" -> "12 11" 
 func(5) "1211" -> "11 12 21"

 class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        count = 2
        last_return = "1"
        # 123141

        # func(1) -> 1
        # func(2) -> 11
        # 3-> 21
        # 4- >1211
        # n^2 -> n = 100, nx -> 100x -> x


func("23456") -> func(23456)
1213141516
11121113111411151116
# nx ,n  x=>2^n   n*    2^n


        while count <= n:
            occurence = 0
            prev_char = None
            # input: 1 1, 2 1
            ans='' # 12
            for char in last_return:
                # this is the first character
                if prev_char == None:
                    occurence = 1

                    prev_char = char # 1, 2
                elif char == prev_char:
                    occurence += 1 # 2
                    prev_char = char
                else:
                    ans += str(occurence) + prev_char # 1, 2
                    occurence = 1
                    prev_char = char # 1 , 11
                    #different character
                    # ??? 
            
            ans+= str(occurence) + prev_char # 11, 21, 11
            last_return = ans
            count += 1 #3, #4
        return last_return
