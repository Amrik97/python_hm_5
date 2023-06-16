def func(n, a1, d, i, res):
    print(res)
    if i == n:
        print("Количество элементов: " + str(n) + ", их сумма: " + str(res))
 return
    i += 1
    a2 = a1 * d
    res += a2
    func(n, a2, d, i, res)


if __name__ == '__main__':
    print("Введите количество элементов: ")
    n = int(input())
    d = -0.5
    a1 = 1

    if n <= 0:
        print("Введите положительное число больше 0!")
        exit()
    func(n, a1, d, 1, a1)