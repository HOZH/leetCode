#
# @lc app=leetcode id=1603 lang=python3
#
# [1603] Design Parking System
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        self.dic = {3: small, 2: medium, 1: big}

    def addCar(self, carType: int) -> bool:

        if self.dic[carType]:
            self.dic[carType] = self.dic[carType]-1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end
