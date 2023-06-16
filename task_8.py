def check(n, a1, res, i):
    if i > n:
        print(res)
        return res
    else:
        res += a1
        a1 += 1
        i += 1
        return check(n, a1, res, i)

if __name__ == '__main__':
    print("Введите натуральное число: ")
    n = int(input())
    right = (n*(n+1))/2
    print(right)
    left = check(n, 1, 0, 1)
    print(left)
    if right == left:
        print("Равенство верное!")
    else:
        print("Равенство неверное!")