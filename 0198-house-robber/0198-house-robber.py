class Solution:
    def rob(self, nums: List[int]) -> int:

        # solving using memoization
        if len(nums) == 1:
            return nums[0]

        memo = [nums[0], max(nums[0], nums[1])]

        def rec(nums):
            if nums:
                memo.append(max(memo[-1], nums[0] + memo[-2]))
                rec(nums[1:])

        rec(nums[2:])

        return memo[-1]

