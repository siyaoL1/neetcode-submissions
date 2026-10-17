class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operands = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            if tokens[i] not in operands:
                numbers.append(int(tokens[i]))
            else:
                operand = tokens[i]
                right = numbers.pop()
                left = numbers.pop()
                if operand == "+":
                    result = left + right
                elif operand == "-":
                    result = left - right
                elif operand == "*":
                    result = left * right
                elif operand == "/":
                    result = left / right
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                numbers.append(result)
        
        return numbers.pop()

        