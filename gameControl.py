#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: gameControl.py
@time: 2018/08/08
"""

from battleUnits import *


class Gamer():

    def __init__(self,unitsList=[],money=10):
        self.unitsList      = unitsList
        self.money          = money
        self.currentResult  = None
        self.currentUnit    = None

        if self.isUnitsSurvive():
            self.currentUnit = unitsList[0]


    def purchaseUnit(self,unitCode):
        """
        :param unitCode: decide which unit to buy
        :return: True = purchase the unit successfully.
        """
        unit = BasicBattleUnit(unitCode=unitCode)
        if self.money >= unit.cost:
            self.money = self.money - unit.cost
            self.unitsList.append(unit)
            self.currentUnit = self.unitsList[0]
            return True
        return False


    def lose(self):
        if not self.isUnitsSurvive():
            return

        self.unitsList.pop(index=0)
        self.currentResult = RESULT_LOSE

    def win(self):
        self.currentResult = RESULT_WIN


    def tie(self):
        if not self.isUnitsSurvive():
            return

        self.unitsList.pop(index=0)
        self.currentResult = RESULT_TIE

    def isUnitsSurvive(self):
        return True if len(self.unitsList)>0 else False


    def __str__(self):
        if self.isUnitsSurvive():
            return self.unitsString()
        else:
            return "No unit has been purchased yet!"

    def unitsString(self):
        string = "current units list:\n"
        i = 1
        for unit in self.unitsList:
            string = string + "{0}.{1} ".format(i, str(unit))
            i+=1

        return string


