#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fives, tens = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True


# @lc code=end

def lemonadeChange(self, bills: List[int]) -> bool:
        bill_dict = {
            5: 0,
            10: 0,
        }
        counter = 0

        
        for bill in bills:
            if bill == 5:
                bill_dict[5] += 1
                counter += 5
            else:
                change_due = bill - 5
                if change_due > counter:
                    return False
                elif bill_dict[5] == 0 and bill_dict[10] == 0:
                    return False
                # missing couple conditions
                else:
                    if change_due >= 15:
                        if bill_dict[10] > 0:
                            bill_dict[10] -= 1
                            bill_dict[5] -= 1
                        elif bill_dict[5] >= 3:
                            bill_dict[5] -= 3
                        else:
                            return False
                    elif change_due >= 10:
                        if bill_dict[10] > 0:
                            bill_dict[10] -=1
                        elif bill_dict[5] >= 2:
                            bill_dict[5] -=2
                        else:
                            return False
                    else:
                        if bill_dict[5] > 0:
                            bill_dict[5] -= 1
                        else:
                            return False

                    
        return True
