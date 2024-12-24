#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_filtered_consecutive_slashes = '/'.join([i for i in path.split('/') if i])
        path_filtered_out_current_dir_dot = list(filter(lambda x: x!='.', path_filtered_consecutive_slashes.split('/')))
        path_filtered_out_prev_dir_dot = []

        for i in path_filtered_out_current_dir_dot:
            if i == '..':
                if len(path_filtered_out_prev_dir_dot) > 0:
                    path_filtered_out_prev_dir_dot.pop()
            else:
                path_filtered_out_prev_dir_dot.append(i)

        return '/' + '/'.join(path_filtered_out_prev_dir_dot)
                


         

        
# @lc code=end

