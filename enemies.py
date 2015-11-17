# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
from hero import *

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy
def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        if answer == "13131313":
            Hero._health += 2000
            print ("вам добавлено 2000 хп")
        else:
            return answer == str(self.__answer)


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
class Trolugadai(Dragon):
    def __init__(self):
        self._health = 400
        self._attack = 20
        self._color = 'Далек'
    def question(self):
        x = randint(1,5)
        at = randint(1,100)/100 + 1
        self._attack *= at
        self.__quest = "Угадай какое число я загадал?"
        self.set_answer(x)
        return self.__quest
def mnogiteli(ch):
    i = 1
    otvet = ""
    while i <= ch//2:
        if ch % i == 0:
            otvet += str(i) + ","
            i += 1
        else:
            i += 1
    else:
        return otvet[:-1]
class Trolmnog(Dragon):
    def __init__(self):
        self._health = 400
        self._attack = 20
        self._color = 'Титан'

    def question(self):
        x = randint(1,100)
        at = randint(1,100)/100 + 1
        self._attack *= at
        self.__quest = str(x) + "- выпиши множители числа через запятую или умрёшь!"
        self.set_answer(mnogiteli(x))
        return self.__quest

def prostch(ch):
    i = 2
    while i < ch:
        if ch % i == 0:
            return 0
        else:
            i += 1
    else:
        return 1
class Trolprost(Dragon):
    def __init__(self):
        self._health = 400
        self._attack = 20
        self._color = 'Тяжеловес'

    def question(self):
        x = randint(1,100)
        at = randint(1,100)/100 + 1
        self._attack *= at
        self.__quest = str(x) + "- простое число?"
        self.set_answer(prostch(x))
        return self.__quest
#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, Trolprost, Trolugadai]