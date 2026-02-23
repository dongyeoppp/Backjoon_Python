row_dict={}
col_dict={}
for i in range(3):
    row, col = map(int,input().split())
    if row not in row_dict:
        row_dict[row] = 1
    else:
        row_dict[row] += 1
    if col not in col_dict:
        col_dict[col] = 1
    else:
        col_dict[col] += 1
result = []
for i in row_dict:
    if row_dict[i] == 1:
        result.append(i)
for i in col_dict:
    if col_dict[i] == 1:
        result.append(i)
print(*result,sep=" ")
