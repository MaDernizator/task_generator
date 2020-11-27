from random import choice
from time import time
import numpy
import math

'''В тексте шаблона в фигурных скобках обозначаются значения, которые необходимо сгенерировать.
После точки с запятой перечисляются диапозоны этих значений, затем - формула ответа, затем
неограниченное количество условий.'''

string = '''На экзамене {c} билетов, Сергей{v} выучил {n} из них. Найдите вероятность того, что ему попадётся выученный билет.;range(6, 100)  ["", " не"]  range(1, 100);1 - n / c if v else n / c; n / c * 10 == int(n / c * 10); n < c'''

class TaskGenerator:
    def __init__(self, pattern, test_mode=False):
        self.test_mode = test_mode
        self.pattern = pattern
        self.text = None
        self.generate()

    def get_text(self):
        return self.text if self.text else False

    def write(self):
        self.text = (eval(f'f\"{self.pattern.split(";")[0]}\"'), answer)

    def check(self):
        for i in self.pattern.split(";")[3:]:
            try:
                if not eval(i.strip()):
                    return False
            except ZeroDivisionError:
                return False
        return True

    def generate(self):
        global answer
        flag = False
        start_time = time()
        error = False
        while not flag:
            if time() - start_time > (5 if not self.test_mode else 2):
                error = True
                break
            for _i, symbol_num in enumerate([i for i, a in enumerate(self.pattern) if a == '{']):
                _s = self.pattern[symbol_num + 1:][:self.pattern[symbol_num + 1:].index('}')]
                exec(f'{_s} = choice({self.pattern.split(";")[1].split("  ")[_i].strip()})',
                     locals(), globals())
            try:
                answer = eval(self.pattern.split(";")[2].strip())
                answer = int(answer) if int(answer) == answer else answer
            except ZeroDivisionError:
                continue
            flag = self.check()
        if not error:
            self.write()

# task = TaskGenerator(string)
# print(task.get_text())