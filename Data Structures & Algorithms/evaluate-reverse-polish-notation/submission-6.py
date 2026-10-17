class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operators = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                numbers.append(int(tokens[i]))
            else:
                operator = tokens[i]
                right = numbers.pop()
                left = numbers.pop()
                if operator == "+":
                    result = left + right
                elif operator == "-":
                    result = left - right
                elif operator == "*":
                    result = left * right
                elif operator == "/":
                    result = left / right
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                numbers.append(result)
        
        return numbers.pop()

        