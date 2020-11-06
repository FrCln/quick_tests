a = 0
q = 1
for i in range(1, 101):
    q *= (100 - i + 1) / 100
    a = q * i / 100
    print(f'{i:3}, {q:5.3f}, {a:5.3f}')
