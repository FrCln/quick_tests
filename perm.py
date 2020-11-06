from itertools import permutations as perm

dg = '234477'

for c in perm(dg):
    n = float('1.0' + ''.join(c)) ** 32
    if abs(int(n) - n) < 0.001:
       print(int(n))