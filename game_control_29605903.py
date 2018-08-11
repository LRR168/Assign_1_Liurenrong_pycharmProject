#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: game_control_29605903.py
@time: 2018/08/09
"""

from battle_units_29605903 import *
import random

def random_int_list(start, stop, length):
    """to create a list of random integer"""
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def prompt_to_continued(prompt,key):
    while True:
        string = input(prompt)
        if (string == key):
            break



class Gamer:

    def __init__(self, money=10, gamer_name="Player"):
        # all units are stored in this list
        self.units_list = []
        self.money = money
        self.current_result = None
        self.current_unit = None
        self.gamer_name = gamer_name


    def purchase_unit(self, unit_code):
        """
        :param unit_code: decide which unit to buy
        :return: True = purchase the unit successfully. False = not enough money.
        """
        unit = BasicBattleUnit(unit_code=unit_code)
        return self.deal_with_a_new_unit(unit)

    def deal_with_a_new_unit(self, new_unit):
        """
        :param new_unit: a unit that the player choose to buy.
        :return: Buying is done or not.
        """
        if self.money >= new_unit.cost:
            self.money = self.money - new_unit.cost
            self.units_list.append(new_unit)
            self.current_unit = self.units_list[0]
            return True
        return False

    def lose(self):
        if not self.has_units_survive():
            return

        died_unit = self.units_list.pop(0)
        self.current_unit = self.units_list[0] if self.has_units_survive() else None
        self.current_result = RESULT_LOSE
        return died_unit

    def win(self):
        self.current_result = RESULT_WIN


    def tie(self):
        if not self.has_units_survive():
            return

        died_unit = self.units_list.pop(0)
        self.current_unit = self.units_list[0] if self.has_units_survive() else None
        self.current_result = RESULT_TIE
        return died_unit

    def has_units_survive(self):
        return True if len(self.units_list) > 0 else False

    def __str__(self):
        if self.has_units_survive():
            return self.units_string()
        else:
            return "No unit has been purchased yet!\n"

    def units_string(self):
        """
        :return: a string like "【 1.KNIGHT 2.KNIGHT 3.SOLDIER 4.ARCHER 5.KNIGHT 6.ARCHER 7.ARCHER 8.ARCHER 9.KNIGHT 10.ARCHER 】"
        """
        string = "\ncurrent units list of {}:\n".format(self.gamer_name)
        i = 1
        units_string = ""
        for unit in self.units_list:
            units_string = units_string + "{0}.{1} ".format(i, str(unit))
            i += 1
        units_string = "【 " + units_string + "】"
        string = string + units_string + "\n{0}: ${1} left.".format(self.gamer_name, self.money)
        return string



class ExtendedGamer(Gamer):
    def __init__(self, money=10, gamer_name="Player"):
        Gamer.__init__(self, money=money, gamer_name=gamer_name)
        self.medics = 0

    def convert_remaining_money_into_medics(self):
        self.medics = int(self.money // 1)
        pass

    """ If an unit has died and the medics left > 0. Resurrect this unit at back of the armies pool"""
    def lose(self):
        died_unit = super().lose()
        if self.medics > 0:
            self.units_list.append(died_unit.reset(died_unit.unit_code))
            self.medics -= 1

    def tie(self):
        died_unit = super().tie()
        if self.medics > 0:
            self.units_list.append(died_unit.reset(died_unit.unit_code))
            self.medics -= 1

    def purchase_unit(self, unit_code):
        """
            Because in extended game, cost of different units varies,
            we have to use ExtendedBattleUnit class.
        """
        unit = ExtendedBattleUnit.unit_factory_with_code(unit_code=unit_code)
        done = self.deal_with_a_new_unit(unit)
        self.convert_remaining_money_into_medics()
        return done




