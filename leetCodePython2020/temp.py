def p(nums, target_count, depth, used, current_list, ans):

            if depth == target_count:
                ans.append(current_list)
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                used[i] = True
                current_list.append(nums[i])
                p(nums, target_count, depth+1, used, current_list[:],ans)
                current_list.pop()
                used[i] = False




result = []
p([1,2,3],3,0,[False,False,False],[],result)
print(result)
