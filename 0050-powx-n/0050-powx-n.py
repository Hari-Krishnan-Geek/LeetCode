class Solution:
    def myPow(self, x: float, n: int) -> float:


        # any number power 0 is 1
        if n == 0:
            return 1

        # if x is a negative number, make it (1/x) and make n positive  
        if n < 0:
            x = 1/x
            n *= -1

        # total = the total number of elements multiplied till now
        total = 1
        # since the total number multiplied is 1, result is x
        result = x

        # variables used for iteration, these will grow exponentially
        count = 1
        prod = x


        # iterate until the total elements multiplied till now are equal to n
        while(total != n):

            # multiplying 'count' number of x's with result is less than pow(x, n)
            if total + count <= n:
                
                # multiply the previous result with a multiple of x
                result *= prod
                # update total number of elements multiplied
                total += count

                # in the next iteration the current result will be multiplied with this updated prod
                prod *= prod
                # count is the number of elements multiplied till now to gecompute current prod 
                count += count

            # multiplying 'count' number of x's with result is greater then pow(x, n),so update count and prod
            else:
                # revisting the exponential growth of count and prod
                count = 1
                prod = x

                
                result *= prod
                total += count

                prod *= prod
                count += count

        return result

