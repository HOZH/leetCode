class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # Calculate prefix sums for even and odd indices
        prefix_even = [0] * (n + 1)
        prefix_odd = [0] * (n + 1)
        
        for i in range(n):
            prefix_even[i + 1] = prefix_even[i] + (nums[i] if i % 2 == 0 else 0)
            prefix_odd[i + 1] = prefix_odd[i] + (nums[i] if i % 2 != 0 else 0)

        count = 0
        for i in range(n):
            even_sum = prefix_even[i] + (prefix_odd[n] - prefix_odd[i + 1])
            odd_sum = prefix_odd[i] + (prefix_even[n] - prefix_even[i + 1])
            if even_sum == odd_sum:
                count += 1

        return count
