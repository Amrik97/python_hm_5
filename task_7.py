import random
def check(n, num ,a ,i):
    if i == n and a != num:
        print("Попытки кончились. Я загадал число : " + str(num))
        return
    elif a == num:
        print("Ты угадал! Загаданное число: " + str(num) + " за " + str(i) + " попыток!")
    return
    else:
        i += 1
        if a > num:
            print("Неправильно, загаданное число меньше! Попробуй ещё :)")
        elif a < num:
            print("Неправильно, загаданное число больше! Попробуй ещё :)")
        print("Введите число: ")
        a = int(input())
        check(n, num, a, i)


if __name__ == '__main__':
    n = 10
    num = random.randint(0, 100)
    print("Я загадал число от 0 до 100, попробуй угадать его)")
    print("Введите число: ")
    a = int(input())
    if a < 0 or a > 100:
        print("Вы ввели число вне диапазона!")
        exit()
    check(n,num,a, 1)