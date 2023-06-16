def mirror(num, reversed_num, pw, rem):
    if pw < 0:
        print("Перевернутое число: " + reversed_num)
        return
    rem = num % 10 #остаток от деления на 10
    reversed_num += str(rem)
    num = num // 10
    pw -= 1
    mirror(num, reversed_num, pw, rem)


if __name__ == '__main__':
    print("Введите число, которое требуется перевернуть: ")
    num = input()
    if int(num) < 10:
        print("Вы ввели однозначное число!")
        exit()
    pw = len(num) - 1 #разрядность числа
    reversed_num = "" #результат в  виде строки
    mirror(int(num), reversed_num, pw, 0)
