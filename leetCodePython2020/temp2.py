class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if nums:
            if lower>nums[0]:
                nums = [n for n in nums if n>lower]
            nums = [lower-1]+nums
            if upper<nums[-1]:
                nums = [n for n in nums if n<upper]
            nums.append(upper+1)
        else:
            nums=[lower-1, upper+1]
            
        for i in range(len(nums)-1):
            print(i)
            if nums[i+1]-nums[i]==2:
                ans.append(str(nums[i]+1))
            elif nums[i+1]-nums[i]>2:
                ans.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        
        return ans


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            return [str(lower)+'->'+str(upper)]
        nums.sort()
        # nums_set = set(nums)
        # current_list = []
        placeholder = []
        # head, tail = 0, float('inf')
        prev, current = 0, 0
        placeholder.append([prev+1, upper])

        for i in range(len(nums)):

            current = nums[i]
            head, tail = prev+1, current-1
            placeholder.append([head, tail])
            prev = current

        placeholder.append([prev+1, upper])
        print(placeholder)

        result = []
        for i in placeholder:
            if i[0] > i[1]:
                continue
            elif i[0] == i[1]:
                result.append(str(i[0]))
            else:
                result.append(str(i[0])+'->'+str(i[1]))

        return result


"""
[-1]
-2
-1

[ -2 ]

"""
