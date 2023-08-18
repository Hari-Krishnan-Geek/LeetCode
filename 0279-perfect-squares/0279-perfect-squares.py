class Solution:
    def numSquares(self, n: int) -> int:
        
        mem = [-1] * (n+1)

        def solve(n):
            if mem[n] != -1:
                return mem[n]
            if n == 0:
                mem[0] = 0
                return mem[0]

            elem = n - 1
            i = 1
            while ((i*i) <= n):
                elem = min(elem, solve(n - (i*i)))
                i += 1
  
            mem[n] = elem + 1
            return mem[n]

        return solve(n)


