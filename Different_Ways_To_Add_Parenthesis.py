expression = input("Enter Expression---> ")
memo = {}

def compute(left, right, operator):
    if operator == '-':
        return left - right
    elif operator == '+':
        return left + right
    elif operator == '*':
        return left * right

def evaluate(expression):
    if expression.isdigit():
        return [int(expression)]

    if expression in memo:
        return memo[expression]

    results = []
    for i in range(len(expression)):
        if expression[i] in "+-*":
            operator = expression[i]
            left_results = evaluate(expression[:i])
            right_results = evaluate(expression[i+1:])

            for left in left_results:
                for right in right_results:
                    results.append(compute(left, right, operator))

    memo[expression] = results
    return results

results = evaluate(expression)
print(results)
