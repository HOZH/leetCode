#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fives = 0
        tens = 0

        for i in range(len(bills)):

            current_bill = bills[i]

            if current_bill == 5:

                fives += 1

            elif current_bill == 10:

                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False

            else:
                if tens > 0 and fives > 0:
                    fives -= 1
                    tens -= 1
                elif fives > 2:
                    fives -= 3

                else:
                    return False

        return True
