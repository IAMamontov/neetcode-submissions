class Solution:
    """Solution"""

    def evalRPN(self, tokens: List[str]) -> int:
        """RPN"""
        operands = []
        for token in tokens:
            if token in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                operands.append(int(token))
            elif token == "+":
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
            elif token == "-":
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                if operand_2 == 0:
                    operands.append(operand_1)
                else:
                    operands.append(operand_1 / operand_2)
        return operands.pop()
    