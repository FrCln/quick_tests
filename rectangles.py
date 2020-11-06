n = 8

res = [[0] * n for i in range(n)]

for i in range(n):
    res[0][i] = res[i][0] = res[i-1][0] + i + 1
    

for i in range(1, n):
    for j in range(1, n):
        res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + (i + 1) * (j + 1)

print(*res, sep='\n')
