def countNumber(m,n):
    result = 0
    for i in range(m, n):
        if (has4(i) == True):
            result = result + 1
    return result


def has4(x):
    while (x != 0):
        if not (x % 10 == 4 or x % 10 == 1 or x % 10 == 9):
            return False
        x = x // 10
    return True




if __name__ == '__main__':
    m = int(input())
    n = int(input())
    result = countNumber(m,n)
    print(result)


