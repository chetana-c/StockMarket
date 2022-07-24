def divisibilityByEleven(num):
    str_num = str(num)
    count = 0
    for i in range(len(str_num)):
        for j in range(len(str_num)):
            my_num = str_num[i:j+1]
            if my_num != '':
                if int(my_num) % 11 == 0:
                    count += 1
    return count

if __name__ == '__main__':
    num = int(input())
    result = divisibilityByEleven(num)
    print(result)