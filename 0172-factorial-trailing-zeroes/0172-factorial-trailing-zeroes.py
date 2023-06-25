class Solution:
    def trailingZeroes(self, n: int) -> int:

        f = 1
        for i in range(2, n+1):
            f *= i

        result = 0
        while f % 10 == 0:
            result += 1
            f = f // 10

        return result

