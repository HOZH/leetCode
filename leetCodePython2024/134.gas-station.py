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
        # gas =  [1,4]
        # cost = [2,3]
        # 0,1,2, 3(possible candidate / correct one), 4(possible candidate + qualify)
        # disqualify 0,1, possible candidates 2,3
        # 2,3,0,1,2 -> 2~3 ,3,0,1,2 -> if we can prove 2~3 is a valid path
        # 
        # 3,0,1,2, 3

        # we know there will always be at least a answer
        # after
        #     if sum(gas) < sum(cost):
        # return -1
        # that means the valid answer contains 0,1,2
        # then if we have potential candidates 3 and 4
        # for 3 as starting point, the valid path will be 3 ... 0,1,2
        # we just need to check the sub path between 3~0

        # if 3 ~ 0 is valid, and 2 ~ 3 is valid, then 2,3,0,1,2 is valid

        
        for i in range(len(gas)):

            if gas[i]+remain_gas < cost[i]: # 1 < 2; 4 < 3
                start = i+1 # 1
                remain_gas = 0 
            else:
                remain_gas += gas[i] # 0 + 4 = 4
                remain_gas -= cost[i] # 4 - 3

        return start
    
    
    def canCompleteCircuit_temp(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        num_of_gas_station = len(gas)
        # gas =  [1,2,3,5,   4]
        # cost = [3,4,5,2,   1]
        visited = set() # visited = [0,1,2]
        for i in range(num_of_gas_station):
            if i in visited:
                continue
            if gas[i] < cost[i]:
                continue
            else:
                remainning_gas = 0
                visited_count = 0
                for j in range(num_of_gas_station+1):
                    next_index = (i+j) % num_of_gas_station
                    if (next_index) == i:
                        visited_count += 1
                        if visited_count == 2:
                            return i
                    remainning_gas += gas[next_index]
                    remainning_gas -= cost[next_index]
                    # print(start, i,j,i+j,next_index, remainning_gas)
                    if remainning_gas < 0:
                        break
                    visited.add(next_index)


                 
            visited.add(i)
        return -1

        
# @lc code=end
# gas =  [1,2,3,4,5]
# cost = [3,4,5,1,2]
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# index 3:
# gas = 4
# cost = 1
# index 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8


def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # cost is how much gas it takes to get to the next station
        # gas is how much you can fill up
        # must refill first and start at 0
        
        index = 0
        total_stations = len(cost)
        valid_index = []

        while index < total_stations:
            tank = 0
            if gas[index] > cost[index]:
                continue
            else:
                valid.append(index)
            index += 1
    
        j = 0
        while j < len(valid_index): # [3, 4]
            start_index = valid_index[j]
            # fill up tank, then compare it to cost
            tank += gas[start_index]

            start_index = (start_index + 1) % total_stations
        # gas = [5, 5, 5, 5, 0] cost = [1,1,1,1,17] -> valid [5,5,5,5] -> return -1
        # 1. gas > cost
        # 2. Key intuitions include knowing that if a trip fails at station C, no station between the start and C is valid, allowing for a single pass

"""
The Gas Station problem is solved in
time by first verifying that total gas exceeds total cost, 
and then using a greedy approach to skip invalid starting points. 

Key intuitions include knowing that if a trip fails at station C, no station between the start and C is valid, 

allowing for a single pass. For a detailed breakdown of this approach, visit 
"""

# example 1# 
# gas =  [1, 1, 1, ....., 1,2,3,..., 4,5] -> valid_stations = [1,1,1, 4,5]
# gas = [1,2,3,4,5] -> valid_stations = [4,    5]
# cost = [3,4,5,1,2]