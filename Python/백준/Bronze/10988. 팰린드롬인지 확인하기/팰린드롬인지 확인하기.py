answer = input()
new_answer = ''.join(reversed(answer))
if answer == new_answer:
    print(1)
else:
    print(0)