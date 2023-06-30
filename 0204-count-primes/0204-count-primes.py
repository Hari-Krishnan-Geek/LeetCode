class Solution:
    def countPrimes(self, n: int) -> int:

        prime = [True for i in range(n)]
        count = 0
        for i in range(2, n):
            if prime[i] == True:
                count += 1
                j = i
                falseList = [False] * (1 + (n -(i*i) - 1)//i)
                prime[i * i: n :i] = falseList
        return count


        