#
# @lc app=leetcode id=2125 lang=python3
#
# [2125] Number of Laser Beams in a Bank
#

# @lc code=start
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        reduced_bank = []
        for row in bank:
            if row.find('1') == -1:
                continue
            reduced_bank.append(row.count('1'))
        ans = 0
        for i in range(1, len(reduced_bank)):
            ans += reduced_bank[i-1]*reduced_bank[i]
        return ans

# @lc code=end
