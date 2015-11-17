# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint
class Hero(Attacker):
    _health = 1000000000000000
    _name = ""
    _attack = 50
    _experience = 0
    def __init__(self,name):
        pass
    def attack(self, target):
        if randint(1,100)>80:
            print('Двойной удар')
            target._health -= self._attack
        target._health -= self._attack
    def gameOver(self):
        pass
#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
