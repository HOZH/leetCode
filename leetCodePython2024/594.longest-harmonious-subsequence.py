#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        bag = defaultdict(int)
        for i in nums:
            bag[i] += 1
        ans = 0
        for i in bag.keys():
            local_count = bag[i]
            if i+1 in bag:
                local_count += bag[i+1]
                ans = max(ans, local_count)

        return ans

# @lc code=end

# 1, 3, 2, 2, 5, 2, 3, 7, 4, 4, 4, 4


1: 1
2: 3 -> key2 + key1 -> 3 + 1 = 4
key2 + key3 -> 3 + 2 = 5
3: 2 -> k3 + k2 = 2 + 3 = 5
k3 + k4 -> 2 + 3 -> 6
4: 4
5: 1
7: 1


find max of  dict[1]+dict[2]+dict[3] dict[2]+dict[3]+dict[4]


find max of  dict[1]+dict[2] = 4

find max of  dict[2]+dict[3] = 5

find max of  dict[5] = 1

max of 7 = 1

1, 3, 2 = 3 -> will not work

1: 1
2: 1
3: 1

1, 2 -> 2
2, 3 -> 2

1, 2, 3 = 3 -> will work


example 2:
[1, 2, 3, 4]

1: 1
2: 1
3: 1
4: 1


[1, 1, 1, 1]
1: 4
1, 1, 2, 1
2, 1, 2, 1
1, 2, 3, 4 -> will not work -> we will get 2 not 4
