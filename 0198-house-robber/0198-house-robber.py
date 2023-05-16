class Solution:
    def rob(self, nums: List[int]) -> int:

        # Solving this problem using dynamic programming
        # dp[i] stores the maximim amount that can be robbed till house 'i'

        n = len(nums)
        if n == 1:
            # if only one house, the maximum amount robbed is the amount in that house alone.
            return nums[0]

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):

            # The maximum amount thant can be robbed as a total is =
            # max(maximum amount that can be robbed till 'i-1' th house, amount in current house +
            # maximum amount that can be robbed till 'i-2' th house)
            dp[i] = max(dp[i-1], (nums[i] + dp[i-2]))

        # returns the maximum amount that can be robbed if we visit all the houses
        return dp[-1]
