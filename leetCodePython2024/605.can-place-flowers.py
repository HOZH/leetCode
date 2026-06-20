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
        count = 0
        compensated_flowerbed = [0]+flowerbed+[0]
        for i in range(1, len(compensated_flowerbed)-1):
            current_status = compensated_flowerbed[i]
            if current_status == 0:
                if compensated_flowerbed[i-1] == 0 and compensated_flowerbed[i+1] == 0:
                    count += 1
                    compensated_flowerbed[i] = 1
            if count == n:
                return True

        return False


# @lc code=end
[1, 0, 0, 0, 0, 0, 1]
n = 2


011111 -> cannot plant at index 0
001111 -> can plant at index 0


def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    total = n
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] != 1:
            left = None
            right = None
            # edge case, first index is 0
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                # handle first index
                flowerbed[i] = 1
                n -= 1
            elif (i == len(flowerbed) - 1) and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                # handle last index
                flowerbed[i] = 1
                n -= 1
            if (i - 1 >= 0 and flowerbed[i - 1] == 0):
                left = flowerbed[i - 1]  # i = 0 , i-1 = -1 which is last index
            if (i + 1 <= len(flowerbed) and flowerbed[i + 1]):
                right = flowerbed[i + 1]
            if left is not None and right is not None and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        i += 1

    print(flowerbed)
    if n == 0:
        return True
    else:
        return False


if ( flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0):
                n-=1
                flowerbed[i]=1
if n == 0:
     return True
