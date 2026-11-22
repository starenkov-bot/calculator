# Автор: Иванов И.И., группа 4ИСП-1, 14.10.2026
def get_number(prompt: str) -> float:
    """
    Запрашивает у пользователя число с проверкой ввода.
    Повторяет запрос, пока не будет введено корректное число.
    """
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введено не число. Попробуйте еще раз.")


def get_operation() -> str:
    """
    Запрашивает у пользователя математическую операцию.
    Повторяет запрос, пока не будет введен один из символов: +, -, *, /
    """
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input("Введите операцию (+, -, *, /): ").strip()
        if op in valid_operations:
            return op
        print("Ошибка: недопустимая операция. Используйте только +, -, *, /.")


def calculate(num1: float, num2: float, operation: str):
    """
    Выполняет математическую операцию и обрабатывает деление на ноль.
    Всегда возвращает кортеж: (результат, сообщение_об_ошибке).
    """
    if operation == '+':
        return num1 + num2, None
    elif operation == '-':
        return num1 - num2, None
    elif operation == '*':
        return num1 * num2, None
    elif operation == '/':
        if num2 == 0:
            return None, "Ошибка: деление на ноль невозможно."
        return num1 / num2, None


def main():
    print("=== Консольный калькулятор ===")
    
    number1 = get_number("Введите первое число: ")
    number2 = get_number("Введите второе число: ")
    operation = get_operation()

    result, error = calculate(number1, number2, operation)

    if error:
        print(error)
    else:
        if result.is_integer():
            result = int(result)
        print(f"Результат: {number1} {operation} {number2} = {result}")


if __name__ == "__main__":
    main()
