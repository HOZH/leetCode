#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries)-1):
            current_starting_time = timeSeries[i]
            next_starting_time = timeSeries[i+1]
            if current_starting_time+duration <= next_starting_time:
                ans += duration
            else:
                ans += next_starting_time - current_starting_time
        # last starting time in timeSeries always last the complete duration
        ans += duration
        return ans

# @lc code=end
def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        output = 0
        curr_dur = timeSeries[0] + duration - 1
        i = 1
        # [1,4] -> output = 2, expecte 4
        # range (last + duration)
        # range: [0, 0, 0,0,0,0] -> [1, 0,0,4,0,0]
        # range: [True, True, 0, True, True, 0]
        while i < len(timeSeries):
            
            prev_time = timeSeries[i - 1]
            curr_time = timeSeries[i]
            if prev_time + duration <= curr_time:
                output += duration
            else:
                diff = curr_time - prev_time
                output += diff
            i += 1            

        return output + duration