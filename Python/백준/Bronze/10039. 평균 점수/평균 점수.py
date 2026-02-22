answer = 0
for i in range(5):
    grade = int(input())
    if grade < 40:
        answer += 40
    else:
        answer += grade
print(answer // 5)