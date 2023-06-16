def output(a, b, n, s, i):
    if a == b:
        s += str(b) + " - " + chr(b)
        print(s)
        return
    if i % n == 0:
        s += "\n"
    s += str(a) + " - " + chr(a)
    i += 1
    a += 1
    output(a, b, n, s, i)


if __name__ == '__main__':
    a = 32
    b = 127
    n = 10
