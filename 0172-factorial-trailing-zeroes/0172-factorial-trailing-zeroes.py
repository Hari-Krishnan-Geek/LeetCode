class Solution:
    def trailingZeroes(self, n: int) -> int:

        x = 5
        result = 0
        while x <= n:
            result += (n // x)
            x *= 5
        return result