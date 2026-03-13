t = int(input())

a=300
b=60
c=10
answer = []

cnt = t//a
t -= cnt * a
answer.append(cnt)

cnt = t//b
t -= cnt*b
answer.append(cnt)

cnt = t//c
t -= cnt*c
answer.append(cnt)
if t !=0:
    print(-1)
else:
    print(*answer)
