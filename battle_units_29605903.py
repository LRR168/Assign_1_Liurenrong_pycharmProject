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

    def __init__(self, unit_code: int=UNIT_UNASSIGNED, cost: int=1):
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
            if self.unit_code < enemy_unit.unit_code:
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
        return self
    def __str__(self):
        return self.unit_name if self.unit_name else super().__str__(self)


class ExtendedBattleUnit(BasicBattleUnit):
    archer_cost = 1
    archer_health = 1

    soldier_cost = 1.75
    soldier_health = 2

    knight_cost = 2.5
    knight_health = 3

    def __init__(self, unit_code: int=UNIT_UNASSIGNED, cost: int=1, health: int=1):
        BasicBattleUnit.__init__(self, unit_code=unit_code, cost=cost)
        self.health = health
        self.previous_health = health
        # a positive value
        self.__current_damage = 0

    def health_greater_than_zero(self):
        return True if self.health > 0 else False

    def get_result_of_combating(self, enemy_unit):
        """ Override the method.
            Considering the health into the each battle, the result of win,
            lose and tie have different meanings compared with results in task1.
            WIN = self.health>0 and enemy.health<0
            LOSE = self.health<0 and enemy.health>0
            TIE = self.health<0 and enemy.health<0
            Therefore, task1's results can be reused and converted to what we need.
        """
        # record the previous health
        self.previous_health = self.health
        enemy_unit.previous_health = enemy_unit.health

        # convert the old results
        result = super().get_result_of_combating(enemy_unit=enemy_unit)
        if result == RESULT_WIN:
            # once set current_damage, the health would minus damage automatically.
            self.current_damage = 1
            enemy_unit.current_damage = 3

        elif result == RESULT_LOSE:
            self.current_damage = 3
            enemy_unit.current_damage = 1

        elif result == RESULT_TIE:
            self.current_damage = 2
            enemy_unit.current_damage = 2

        # judge the new results
        if self.health > 0:
            if enemy_unit.health <= 0:
                return RESULT_WIN
            else:
                # Both got health > 0 only if 2 knights encounter.
                pass
        else:
            if enemy_unit.health > 0:
                return RESULT_LOSE
            else:
                return RESULT_TIE

    def reset(self, unit_code):
        super().reset(unit_code)
        self.__current_damage = 0
        if unit_code == UNIT_ARCHER:
            self.cost = self.archer_cost
            self.health = self.archer_health

        elif unit_code == UNIT_SOLDIER:
            self.cost = self.soldier_cost
            self.health = self.soldier_health

        elif unit_code == UNIT_KNIGHT:
            self.cost = self.knight_cost
            self.health = self.knight_health

        return self

    def __str__(self):
        # like "ARCHER(2HP)"
        return (self.unit_name + "(" + str(self.previous_health) + "HP)") if self.unit_name else super().__str__(self)

    @property
    def current_damage(self):
        return self.__current_damage

    @current_damage.setter
    def current_damage(self, value):
        self.__current_damage = value
        self.health -= value

    @classmethod
    def unit_factory_with_code(cls, unit_code):
        if unit_code == UNIT_ARCHER:
            return ExtendedBattleUnit(unit_code=UNIT_ARCHER, cost=cls.archer_cost, health=cls.archer_health)
        elif unit_code == UNIT_SOLDIER:
            return ExtendedBattleUnit(unit_code=UNIT_SOLDIER, cost=cls.soldier_cost, health=cls.soldier_health)
        elif unit_code == UNIT_KNIGHT:
            return ExtendedBattleUnit(unit_code=UNIT_KNIGHT, cost=cls.knight_cost, health=cls.knight_health)
        else:
            return None

