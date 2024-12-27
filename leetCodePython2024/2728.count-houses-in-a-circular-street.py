#
# @lc app=leetcode id=2728 lang=python3
#
# [2728] Count Houses in a Circular Street
#

# @lc code=start
# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:

        houses_have_seen = 0

        while houses_have_seen <= k:
            if street.isDoorOpen():
                street.closeDoor()
            houses_have_seen += 1
            street.moveRight()

        ans = 0
        while not street.isDoorOpen():
            street.openDoor()
            ans += 1
            street.moveRight()

        return ans


# @lc code=end
