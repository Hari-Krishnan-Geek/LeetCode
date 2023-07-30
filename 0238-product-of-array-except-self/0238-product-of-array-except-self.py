class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l = [1] * n
        r = [1] * n

        prod1 = 1
        prod2 = 1
        for i in range(n):

            l[i] = prod1
            prod1 *= nums[i]

            r[-(i+1)] = prod2
            prod2 *= nums[-(i+1)]

        result = [1] * n
        for i in range(n):
            result[i] = l[i] * r[i]

        return result


        

        