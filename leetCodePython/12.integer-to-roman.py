#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:


    def intToRoman(self,num: int) -> str:

        result = ''

    # dic = {
    #     1: 'I',
    #     5: 'V',
    #     10: 'X',
    #     50: 'L',
    #     100: 'C',
    #     500: 'D',
    #     1000: 'M'
    # }

        while num>0:  # coulda use a switch here instrad

        # print(num,'abc')

            if num>=100:
                if num >= 1000:
                    num -= 1000
                    result += 'M'

                elif num >= 900:
                    num -= 900
                    result += 'CM'

                elif num >= 500:
                    num -= 500
                    result += 'D'

                elif num >= 400:
                    num -= 400
                    result += 'CD'

                elif num >= 100:
                    num -= 100
                    result += 'C'
            
            else:

                if num >= 90:
                    num -= 90
                    result += 'XC'

                elif num >= 50:
                    num -= 50
                    result += 'L'

                elif num >= 40:
                    num -= 40
                    result += 'XL'

                elif num >= 10:
                    num -= 10
                    result += 'X'

                elif num >= 9:
                    num -= 9
                    result += 'IX'

                elif num >= 5:
                    num -= 5
                    result += 'V'

                elif num >= 4:
                    num -= 4
                    result += 'IV'

                elif num >= 1:
                    num -= 1
                    result += 'I'

            # if num == 0:
            #     break

        return result
        

