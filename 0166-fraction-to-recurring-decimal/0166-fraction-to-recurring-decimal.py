class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:


        sign =  ""
        if numerator * denominator < 0:
            sign = "-"
        numerator, denominator = abs(numerator), abs(denominator)
        inti = int(numerator / denominator)
        reminder = numerator % denominator
                
        inti = sign + str(inti)

        if reminder == 0:
            return inti

        result = inti + "."
        seen = {}
        decimal = ""
        while reminder:
            if reminder in seen.keys():
                common = "(" + decimal[seen[reminder]:] + ")"
                decimal = decimal[:seen[reminder]] + common
                return result + decimal
            else:
                seen[reminder] = len(decimal)
                numerator = reminder * 10
                inti = abs(int(numerator / denominator))
                reminder = numerator % denominator
                decimal += str(inti)

        return result + decimal






        

