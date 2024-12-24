#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        last_encoded_str = self.countAndSay(n-1)
        rle_str = ''
        count, val = 0, None
        for i in last_encoded_str:
                if val == None:
                    val = i
                    count = 1
                elif val == i:
                    count += 1
                else:
                    rle_str += str(count)+val
                    val = i
                    count = 1
        rle_str += str(count) + val
        return rle_str

# @lc code=end
