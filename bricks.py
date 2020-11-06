c = [0]
for i in range(10000):
    c.append(sum(x + 0.5 for x in c) / len(c))
   
print(*c, sep='\n')
