def calculator():
    m = ["+", "-", "*", "/", "0"]
    print("Введите операцию (+, -, *, / или 0 для выхода): ")
    operator = input()
    if not (operator in m):
        print("Вы ввели неизвестную операцию")
        calculator()
    elif operator == "0":
        print("Выход")
        exit()
    print("Введите первое число: ")
    try:
        a = int(input())
    except ValueError:
        print("Вы ввели строку вместо числа")
        calculator()
    print("Введите второе число: ")
    try:
        b = int(input())
    except ValueError:
        print("Вы ввели строку вместо числа")
  calculator()
    match operator:
        case "+":
            res = a + b
            print("Ваш результат: " + str(res))
        case "-":
            res = a - b
            print("Ваш результат: " + str(res))
        case "*":
            res = a * b
            print("Ваш результат: " + str(res))
        case "/":
            if b == 0:
                print("Нельзя делить на 0!")
       calculator()
            else:
                res = a / b
                print("Ваш результат: " + str(res))


if __name__ == '__main__':
    calculator()
