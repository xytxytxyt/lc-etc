# ctci edition 6 pg 524

operators_higher = ['*', '/']
operators_lower = ['+', '-']
operators = operators_higher + operators_lower


def lex(s):
    tokens = []
    current_start = 0
    for i in range(len(s)):
        c = s[i]
        if c in operators:
            operand = float(s[current_start:i])
            operator = s[i]
            tokens.append(operand)
            tokens.append(operator)
            current_start = i + 1
    tokens.append(float(s[current_start:]))
    return tokens


def compute(tokens):
    if tokens[1] == '+':
        return tokens[0] + tokens[2]
    elif tokens[1] == '-':
        return tokens[0] - tokens[2]
    elif tokens[1] == '*':
        return tokens[0] * tokens[2]
    elif tokens[1] == '/':
        return tokens[0] / tokens[2]


def interpret(tokens, last_higher_operator_i=None):
    if last_higher_operator_i is None:
        last_higher_operator_i = 0

    if len(tokens) == 1:
        return tokens[0]
    elif len(tokens) == 3:
        return compute(tokens)
    else:
        next_processed_operator = None
        for i in range(last_higher_operator_i, len(tokens)):
            if tokens[i] in operators_higher:
                next_processed_operator = tokens[i]
                last_higher_operator_i = i
                break
        if next_processed_operator is None:
            next_processed_operator = tokens[1]

        i = tokens.index(next_processed_operator)
        tokens_next = tokens[:(i - 1)]
        tokens_next.append(compute([tokens[i - 1], tokens[i], tokens[i + 1]]))
        tokens_next += tokens[(i + 2):]
        return interpret(tokens_next, last_higher_operator_i)


assert lex('2*3+5/6*3+15') == [2.0, '*', 3.0, '+', 5.0, '/', 6.0, '*', 3.0, '+', 15.0]
assert interpret([2.0, '*', 3.0]) == 6.0
assert interpret([2.0]) == 2.0
assert interpret([2.0, '*', 3.0, '*', 4.0]) == 24.0
assert interpret([2.0, '*', 3.0, '+', 5.0, '/', 6.0, '*', 3.0, '+', 15.0]) == 23.5
