#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        # input abcd efg
        # only process first 4 elements
        # abcd=>bacd
        # length = 7
        # stop_index = 7 // (2*2) * (2*2) = 1 * 4 = 4
        stop_index =len(s)//(2*k)*2*k
        ans = []
        for i in range(0,stop_index,2*k):
            ans.extend(s[i:i + k][::-1])
            # to not reverse
            ans.extend(s[i + k:i + 2 * k])


        # need to process 'efg'
        # efg => fe g

        # must less than 2*k elements left
        # remaining elements are greater or equals to k 
        # 7 - 4 >=k => 7 -4 >= 2 => true
        if length - stop_index>=k:
            # only reverse first k elements
            ans.extend(s[stop_index:stop_index + k][::-1])
            ans.extend(s[stop_index + k:])

        # remaining elements are less than k
        else:
            ans.extend(s[stop_index:][::-1])

        return ''.join(ans)

        
# @lc code=end

