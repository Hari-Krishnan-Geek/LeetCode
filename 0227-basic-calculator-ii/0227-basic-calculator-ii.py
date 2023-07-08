class Solution:
    def calculate(self, s: str) -> int:

        def getPriority(x):
            if x in ["*", "/"]:
                return 2
            if x in ["+", "-"]:
                return 1

        def operate(a, b, op):
            if op == "*":
                return a * b
            if op == "/":
                return int(a / b)
            if op == "+":
                return a + b
            if op == "-":
                return a - b

        stack = []
        result = []
        num = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            else:
                if i == " ":
                    continue

                result.append(num)
                num = 0

                # if stack is non empty, then there must atleast be two operands in result
                while stack and getPriority(stack[-1]) >= getPriority(i):
                    b = result.pop()
                    a = result.pop()
                    op = stack.pop()
                    result.append(operate(a, b, op))
                stack.append(i)


        result.append(num)
        while stack:
            b = result.pop()
            a = result.pop()
            op = stack.pop()
            result.append(operate(a, b, op))
        
        return result[0]

                        


                
