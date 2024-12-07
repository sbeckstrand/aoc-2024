from itertools import product
import operator


OPERATORS = {
    "+": operator.add,
    "*": operator.mul
}

def operate(answer: int, numbers: list[int], operations: list[str]) -> bool:

    # create product of all possible combinations of operations [(+, +), (+, *), ...]
    op_combos = product(operations, repeat=(len(numbers) - 1))

    # For each combination of operations, calculate result using given operations
    for combo in op_combos:
        combo = list(combo)
        result = numbers[0]
        for i, op in enumerate(combo):
            if op == "||":
                result = int(str(result) + str(numbers[i + 1]))
            else: 
                result = OPERATORS[op](result, numbers[i + 1])
        if result == answer:
            return True
        
    # If no combination resulted in the answer, return False
    return False

# For each equation that has a possible combination to get answer, add the answer to total and return it
def calc_total(equations: list[str], operations: list[str]) -> int:
    total = 0
    for equation in equations:
        answer, numbers = equation
        if operate(answer, numbers, operations):
            total += answer
 
    return total

def main():
    
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()

    equations = []
    for line in input_data.split("\n"):
        answer = int(line.split(":")[0])
        numbers = [int(num) for num in line.split(":")[1].strip().split(" ")]
        equations.append((answer, numbers))
    
    p1 = calc_total(equations, ["+", "*"])
    p2 = calc_total(equations, ["*", "+", "||"])

    return (p1, p2)

print(main())