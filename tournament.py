# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = input(message)
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                hero._experience += 10
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                if hero._experience >= 5:
                    hero._experience -= 5
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
        re = open("expirence_reiting.txt","r")
        gamers = re.readlines()
        gamers.remove(len(gamers)-1)
        expe = [(k.split())[1] for k in gamers]
        expe.sort()
        i = len(expe) - 1
        place = 1
        while hero._experience <= expe[i]:
            place += 1
            i -= 1
        else:
            print ("Вы заняли " + str(place) + "-е место")
        exp = open("expirence_reiting.txt","w")
        text = hero._name +" " + str(hero._experince) + "\n"
        exp.write(text)

    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и троллями!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 5
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 5)
        print('У Вас на пути', dragon_number, 'драконов и троллей!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
