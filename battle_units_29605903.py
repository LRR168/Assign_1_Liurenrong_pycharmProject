#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: battle_units_29605903.py
@time: 2018/08/09
"""


UNIT_UNASSIGNED = 0
UNIT_ARCHER     = 1
UNIT_SOLDIER    = 2
UNIT_KNIGHT     = 3

RESULT_WIN      = 100
RESULT_LOSE     = 200
RESULT_TIE      = 300


class BasicBattleUnit:

    """  x  """

    def __init__(self,unit_code: int=UNIT_UNASSIGNED,cost:int=1):
        self.unit_code = unit_code
        self.cost = cost
        self.unit_name = self.get_name(unit_code)

    def get_name(self,unit_code):
        """
        :param unitCode: This is a unique code that can identify type of units.

        """
        if unit_code == UNIT_ARCHER:
            return "ARCHER"
        elif unit_code == UNIT_SOLDIER:
            return "SOLDIER"
        elif unit_code == UNIT_KNIGHT:
            return "KNIGHT"
        else:
            return "Not setup yet."

    def get_result_of_combating(self, enemy_unit):
        """
        :param enemyUnit: A enemy unit that this unit will combat.
        :return: result of combating: 0,1,2 represent win,lose,tie separately.
        """

        if self.unit_code == enemy_unit.unit_code:
            # Two units are the same type.
            return RESULT_TIE

        if self.unit_code * enemy_unit.unit_code == 3:
            # Special case: one unit is ARCHER and another one is KNIGHT.
            if self.unitCode < enemy_unit.unit_code:
                # self = ARCHER and enemy = KNIGHT
                return RESULT_LOSE
            else:
                # self = KNIGHT and enemy = ARCHER
                return RESULT_WIN

        return RESULT_WIN if self.unit_code < enemy_unit.unit_code else RESULT_LOSE

    def reset(self, unit_code):
        """
        To reset the status of the instance in case it need to be reused.
        """
        self.unit_code = unit_code
        self.unit_name = self.get_name(unit_code)

    def __str__(self):
        return self.unit_name if self.unit_name else super().__str__(self)

