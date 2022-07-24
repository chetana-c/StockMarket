def checkPalin(str,i,j):
    while i<j :
        if str[i] != str[j]:
            return False
        i+=1
        j-=1
    return True

def addChar(str):
    for i in range(len(str)):
        if(checkPalin(str,i,len(str)-1)):
            return None
        rev = str[::-1]
        return rev[1:]


if __name__ == '__main__':
    str = input()
    result = addChar(str)
    print(result)