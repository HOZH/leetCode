#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        # alway has a ans if sum(gas)>=sum(cost)
        start = 0
        remain_gas = 0

        for i in range(len(gas)):

            if gas[i]+remain_gas < cost[i]:
                start = i+1
                remain_gas = 0
            else:
                remain_gas += gas[i]
                remain_gas -= cost[i]

        return start

# @lc code=end
