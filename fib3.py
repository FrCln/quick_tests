fib = [1, 1]
fr = [1, 1]

for i in range(38):
    f = fib[-1] + fib[-2]
    f1 = fr[-1] + fr[-2] + 1
    fib.append(f)
    fr.append(f1)
    print(f'{f:10}{f1:10}')