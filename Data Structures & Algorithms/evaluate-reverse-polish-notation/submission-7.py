class Solution:
    """Solution"""

    def evalRPN(self, tokens: List[str]) -> int:
        """RPN"""
        operands = []
        for token in tokens:
            if token == "+":
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                operands.append(operand_1 + operand_2)
            elif token == "-":
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                operands.append(operand_1 - operand_2)
            elif token == "*":
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                operands.append(operand_1 * operand_2)
            elif token == "/":
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                if operand_2 == 0:
                    operands.append(operand_1)
                else:
                    operands.append(int(operand_1 / operand_2))
            else:
                operands.append(int(token))
        return operands.pop()
    