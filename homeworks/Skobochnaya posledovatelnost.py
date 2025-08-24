from inspect import stack


def RPN(expression):
    stack = []
    tokens = expression.split()


        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # Если токен - число, помещаем его в стек
                stack.append(float(token))
        else:
            # Если токен - оператор, извлекаем из стека два верхних элемента и выполняем операцию
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Ошибка: деление на ноль.")
                result = operand1 / operand2
            else:
                raise ValueError(f"Ошибка: неизвестный оператор '{token}'.")

            # Помещаем результат обратно в стек
            stack.append(result)

        # На выходе в стеке должен остаться единственный элемент - результат вычисления
        if len(stack) != 1:
            raise ValueError("Ошибка: неверное выражение.")

        return stack.pop()

# Считываем строку
# Пример использования
input_expression = input("Введите выражение в обратной польской записи: ")
    result = evaluate_rpn(input_expression)
    print(f"Результат: {result}")