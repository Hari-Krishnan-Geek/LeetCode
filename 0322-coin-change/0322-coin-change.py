class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        result = [amount+1] * (amount+1)

        for each in coins:
            if len(result) > each:
                result[each] = 1

        for i in range(len(result)):
            for each in coins:
                if i - each < 0:
                    continue
                result[i] = min(result[i], result[i-each] + 1)

        if result[amount] == amount + 1:
            return -1
        else:
            return result[amount]