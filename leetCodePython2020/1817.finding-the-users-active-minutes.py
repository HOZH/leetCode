#
# @lc app=leetcode id=1817 lang=python3
#
# [1817] Finding the Users Active Minutes
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:


        logs = set(map(lambda x:tuple(x),logs))

        users = defaultdict(int)


        for i,_ in logs:
            users[i]+=1


        ans = [0]*k

        for _,j in users.items():
            ans[j-1]+=1

        return ans

        
# @lc code=end

