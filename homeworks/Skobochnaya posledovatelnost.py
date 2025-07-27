def is_balanced(a):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in a:
        if char in brackets.values():
            # Если символ - открывающая скобка, добавляем в стек
            stack.append(char)
        elif char in brackets.keys():
            # Если символ - закрывающая скобка
            if stack and stack[-1] == brackets[char]:
                # Если верхняя открывающая скобка соответствует закрывающей, убираем её
                stack.pop()
            else:
                # Если нет соответствия, последовательность неправильная
                return False

    # Если стек пуст, значит все скобки были корректно закрыты
    return len(stack) == 0

# Считываем строку
input_string = input("Введите строку со скобками: ")
if is_balanced(input_string):
    print("Строка является правильной скобочной последовательностью.")
else:
    print("Строка является неправильной скобочной последовательностью.")