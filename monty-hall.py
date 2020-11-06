from random import shuffle, choice


class Monty:
    def __init__(self):
        self.vars = [1, 0, 0]
        shuffle(self.vars)
        
    def open(self, var):
        assert var in (0, 1, 2)
        return choice([x for x in range(3) if x != var and not self.vars[x]])
        
    def check(self, var):
        return self.vars[var]
        

stat1 = 0
for _ in range(1000):
    m = Monty()
    stat1 += m.check(1)
    
stat2 = 0
for _ in range(1000):
    m = Monty()
    v = 2 - m.open(1)
    stat2 += m.check(v)

print(stat1, stat2)
