def gcd():
    global result,a,b
    if a >= b:
        for i in range(2,b+1):
            if a % i ==0 and b % i ==0:
                result = result * i
                a = a // i
                b = b // i
                return True
        return False
    else:
        for i in range(2,a+1):
            if a % i ==0 and b % i ==0:
                result = result * i
                a = a // i
                b = b // i
                return True
        return False

t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    result = 1
    while gcd():
        if a == 1 or b == 1:
            break
    result = result * a
    result = result * b
    print(result)
