def summa(a, b, i, res):
    if i == b:
        print(str(a) + " + " + str(b) + " = " + str(res))
  return
    i += 1
    res += 1
    summa(a, b, i, res)


if __name__ == '__main__':
    print("Введите первое целое неотрицательное число: ")
    try:
        a = int(input())
        if a < 0:
            print("Вы ввели отрицательное число!")
            exit()
    except ValueError:
        print("Вы ввели не целое число!")
        exit()
    print("Введите второе целое неотрицательное число: ")
    try:
        b = int(input())
        if b < 0:
            print("Вы ввели отрицательное число!")
            exit()
    except ValueError:
        print("Вы ввели не целое число!")
        exit()
    summa(a, b, 0, a)