#
# @lc app=leetcode id=2224 lang=python3
#
# [2224] Minimum Number of Operations to Convert Time
#

# @lc code=start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        correct_hr,correct_mint = correct.split(':')
        hr,mint = current.split(':')
        correct_hr, correct_mint = int(correct_hr), int(correct_mint)
        hr, mint = int(hr), int(mint)

        ans = correct_hr-hr
        if mint>correct_mint:
            ans-=1
            correct_mint+=60-mint
            mint = 0
        
        options = (60,15,5,1)
        temp = correct_mint-mint
        for i in options:
            while i<=temp:
                ans+=1
                temp-=i
                if temp==0:
                    break
        return ans

        
# @lc code=end

