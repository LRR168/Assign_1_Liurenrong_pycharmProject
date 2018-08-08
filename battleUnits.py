#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: battleUnits.py
@time: 2018/08/08
"""

UNIT_UNASSIGNED = 0
UNIT_ARCHER     = 1
UNIT_SOLDIER    = 2
UNIT_KNIGHT     = 3

RESULT_WIN      = 100
RESULT_LOSE     = 200
RESULT_TIE      = 300

class BasicBattleUnit():
    """  x  """

    def __init__(self, unitCode = UNIT_UNASSIGNED, cost=1):
        self.unitCode = unitCode
        self.cost = cost
        self.unitName = self.__getName(unitCode)


    def __getName(self,unitCode):
        """
        :param unitCode: This is a unique code that can identify type of units.

        """
        if unitCode == UNIT_ARCHER:
            return "ARCHER"
        elif unitCode == UNIT_SOLDIER:
            return "SOLDIER"
        elif unitCode == UNIT_KNIGHT:
            return "KNIGHT"
        else:
            return "Not setup yet."


    def getResultOfCombating(self, enemyUnit):
        """
        :param enemyUnit: A enemy unit that this unit will combat.
        :return: result of combating: 0,1,2 represent win,lose,tie separately.
        """

        if self.unitCode == enemyUnit.unitCode:
            # Two units are the same type.
            return RESULT_TIE

        if self.unitCode * enemyUnit.unitCode == 3:
            # Special case: one unit is ARCHER and another one is KNIGHT.
            if self.unitCode < enemyUnit.unitCode:
                # self = ARCHER and enemy = KNIGHT
                return RESULT_LOSE
            else:
                return RESULT_WIN

        return RESULT_WIN if self.unitCode < enemyUnit.unitCode else RESULT_LOSE


    def reset(self, unitCode):
        """
        To reset the status of the instance in case it need to be reused.
        """
        self.unitCode = unitCode
        self.unitName = self.__getName(unitCode)


    def __str__(self):
        return self.unitName if self.unitName else "lrrrrrrrrrr"