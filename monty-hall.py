from random import shuffle, choice


class Monty:
    """ Ведущий игры. """
    def __init__(self):
        self.vars = [1, 0, 0]
        shuffle(self.vars)
        
    def open(self, var):
        """
        Открытие двери. На вход продается номер двери, выбранной игроком.
        Возвращает номер другой двери, за которой ничего нет
        """
        assert var in (0, 1, 2)
        return choice([x for x in range(3) if x != var and not self.vars[x]])
        
    def check(self, var):
        """ Возвращает 1 в случае победы, 0 в случае поражения """
        return self.vars[var]
        

# Первый игрок просто открывает произвольную дверь
stat1 = 0
for _ in range(1000):
    m = Monty()
    stat1 += m.check(1)
    
# Второй игрок всегда меняет дверь после подсказки
stat2 = 0
for _ in range(1000):
    m = Monty()
    v = 2 - m.open(1)
    stat2 += m.check(v)

print(stat1, stat2)
# -> 333 666 или около того
