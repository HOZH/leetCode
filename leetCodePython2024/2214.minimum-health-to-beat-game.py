#
# @lc app=leetcode id=2214 lang=python3
#
# [2214] Minimum Health to Beat Game
#

# @lc code=start
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_dmg_can_block = 0
        for i in damage:
            if i <= armor:
                max_dmg_can_block = max(max_dmg_can_block, i)
            else:
                max_dmg_can_block = armor

        return sum(damage)-max_dmg_can_block+1

# @lc code=end
