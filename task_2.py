def counter(num, even, odd):
    if num == 0:
        print("Количество четных и нечетных цифр в числе равно: " + "(" + str(
            even) + "," + str(odd) + ")")
        return
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
    counter(num, even, odd)


if __name__ == '__main__':
    print("Введите число: ")
    num = int(input())
    even, odd = 0, 0
    counter(num, even, odd)


def power(num, pw, i, res):
    if i == pw:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(res))
        return
    i += 1
    res *= num
    power(num, pw, i, res)


if __name__ == '__main__':
    print("Введите натуральное число которое нужно возвести в степень: ")
    try:
        num = int(input())
    except ValueError:
        print("Вы ввели не целое число!")
        exit()
    print("Введите степень числа: ")
    try:
        pw = int(input())
    except ValueError:
        print("Вы ввели не целое число!")
        exit()
    if num == 0:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(0))
        exit()
    elif pw == 0:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(1))
        exit()
    elif pw == 1:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(num))
        exit()
    power(num, pw, 1, num)