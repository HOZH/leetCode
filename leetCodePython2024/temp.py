

nums_and_operators = []
prev = expression[0]
for i in range(1, len(expression)):
        current = expression[i]
        is_current_numeric = current.isdigit()
        if is_current_numeric:
            if prev.isdigit():
                prev += current
            else:
                nums_and_operators.append(prev)
                prev = current
        else:
            nums_and_operators.append(prev)
            prev = current

nums_and_operators.append(prev)

def get_operation_result(num1, num2, op):
    match op:
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        case '*':
            return num1*num2




def multiply(a: list, b: list, operator) -> list: 
    c = []
    