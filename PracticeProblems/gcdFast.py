def gcd(a, b):
    if(a == 0):
        return b
    elif(b == 0):
        return a
    while(a > 0 and b > 0):
        if(a >= b):
            a = a % b
        else:
            b = b % a
    return max(a, b)

if(__name__ == "__main__"):
    a, b = map(int, input().split())
    print(gcd(a, b))
