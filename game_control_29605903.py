#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: game_control_29605903.py
@time: 2018/08/09
"""

from battle_units_29605903 import *


class Gamer:

    def __init__(self,money=10,gamer_name="Player"):
        self.units_list = []
        self.money = money
        self.current_result = None
        self.current_unit = None
        self.gamer_name = gamer_name


    def purchase_unit(self,unit_code):
        """
        :param unit_code: decide which unit to buy
        :return: True = purchase the unit successfully.
        """
        unit = BasicBattleUnit(unit_code=unit_code)
        if self.money >= unit.cost:
            self.money = self.money - unit.cost
            self.units_list.append(unit)
            self.current_unit = self.units_list[0]
            return True
        return False


    def lose(self):
        if not self.has_units_survive():
            return

        self.units_list.pop(0)
        self.current_unit = self.units_list[0] if self.has_units_survive() else None
        self.current_result = RESULT_LOSE

    def win(self):
        self.current_result = RESULT_WIN


    def tie(self):
        if not self.has_units_survive():
            return

        self.units_list.pop(0)
        self.current_unit = self.units_list[0] if self.has_units_survive() else None
        self.current_result = RESULT_TIE

    def has_units_survive(self):
        return True if len(self.units_list)>0 else False


    def __str__(self):
        if self.has_units_survive():
            return self.units_string()
        else:
            return "No unit has been purchased yet!"

    def units_string(self):
        string = "\ncurrent units list of {}:\n".format(self.gamer_name)
        i = 1
        units_string = ""
        for unit in self.units_list:
            units_string = units_string + "{0}.{1} ".format(i, str(unit))
            i+=1
        units_string = "【 " + units_string + "】"
        string = string + units_string + "\n{0}: ${1} left.".format(self.gamer_name, self.money)
        return string





