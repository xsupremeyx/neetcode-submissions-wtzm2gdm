class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                elem2 = stack.pop()
                elem1 = stack.pop()
                elem3 = elem2 + elem1
                stack.append(elem1)
                stack.append(elem2)
                stack.append(elem3)
            elif op == 'D':
                elem = stack.pop()
                stack.append(elem)
                stack.append(elem*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)