class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        prev = nums[0]
        next_insertion_index = 1

        for i in range(1, len(nums)):
            current = nums[i]
            if current == prev:
                continue
            else:
                prev = current
                nums[next_insertion_index] = current
                next_insertion_index += 1

        return next_insertion_index



temp = [item for small_list in big_list for item in small_list]


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: x != '', s.split(' ')))[-1])
