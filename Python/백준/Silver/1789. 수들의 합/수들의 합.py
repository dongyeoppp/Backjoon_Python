s = int(input())
answer = 1
cnt = 0
while s >= 0:
    s -= answer
    cnt += 1
    answer +=1
print(cnt-1)