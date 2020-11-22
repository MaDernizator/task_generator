from random import choice
from time import time

string = '''Катер движется {n}. За сколько часов он преодолеет растояние в {s} км, если собственная скорость катера равна {vk} км/ч, а скорость течения {vt} км/ч?; ["по течению", "против течения"]  range(5, 150)  range(5, 25)  range(2, 7); s / (vk + vt) if n == "по течению" else s / (vk - vt); type(answer) == int; (vt + vk) % 3 == 0'''

'''В тексте шаблона в фигурных скобках обозначаются значения, которые необходимо сгенерировать.
После точки с запятой перечисляются диапозоны этих значений, затем - формула ответа, затем
неограниченное количество условий.'''


class TaskGenerator:
    def __init__(self, pattern):
        self.pattern = pattern
        self.text = None
        self.generate()

    def get_text(self):
        return self.text

    def write(self):
        self.text = (eval(f'f\"{self.pattern.split(";")[0]}\"'), answer)
        # print(self.text)

    def check(self):  # TODO добавить ограничение по времени
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
        while not flag:
            if time() - start_time > 5:
                pass #TODO дописать ошибку
            for _i, symbol_num in enumerate([i for i, a in enumerate(self.pattern) if a == '{']):
                _s = self.pattern[symbol_num + 1:][:self.pattern[symbol_num + 1:].index('}')]
                exec(f'{_s} = choice({self.pattern.split(";")[1].split("  ")[_i].strip()})', locals(),
                    globals())
            try:
                answer = eval(self.pattern.split(";")[2].strip())
                answer = int(answer) if int(answer) == answer else answer
            except ZeroDivisionError:
                continue
            flag = self.check()
        self.write()


g = TaskGenerator(string)
