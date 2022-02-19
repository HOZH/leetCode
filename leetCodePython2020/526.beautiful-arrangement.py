#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:

        self.lis = set([i for i in range(1, n + 1)])
        self.count = 0

        def helper(temp_lis):
            if temp_lis.count(0) == 1:
                self.count += 1
                return
            for i in range(1, n + 1):
                if temp_lis[i] == 0:
                    for chosen in list(self.lis):
                        if i % chosen == 0 or chosen % i == 0:
                            new_temp_lis = list(temp_lis)
                            new_temp_lis[i] = chosen
                            self.lis.remove(chosen)
                            helper(new_temp_lis)
                            self.lis.add(chosen)
                    break

        helper([0 for _ in range(n + 1)])
        return self.count
      


        
# @lc code=end

