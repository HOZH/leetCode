#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        current_index, prev_index, next_index = 0, -1, 1

        while next_index <= len(flowerbed):

            if flowerbed[current_index] != 1:
                if (prev_index < 0 or flowerbed[prev_index] == 0) and (next_index == len(flowerbed) or flowerbed[next_index] == 0):
                    flowerbed[current_index] = 1
                    n -= 1
                    if (n == 0):
                        return True
            prev_index = current_index
            current_index = next_index
            next_index += 1
        return False


        
# @lc code=end

