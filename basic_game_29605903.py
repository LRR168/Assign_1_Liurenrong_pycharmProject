#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: basic_game_29605903.py
@time: 2018/08/08
"""

# import random
# import math
#
# print(random.randint(1,10))
# print(math.pi)
# print("sdfsdfasdfwefs".count("s"))


from gameControl import *


gamer = Gamer()

# process of purchasing units
codeList = [UNIT_ARCHER,UNIT_SOLDIER,UNIT_KNIGHT]

for i in range(10):

    print(gamer)
    while(True):
        unitCode = input(
            "please purchase an unit placed in the {0} poisition: {1} for ARCHER,"
            "{2} for SOLDIER,{3} for KNIGHT:\n"
            .format(i + 1, UNIT_ARCHER, UNIT_SOLDIER, UNIT_KNIGHT))

        if int(unitCode) in codeList:
            gamer.purchaseUnit(int(unitCode))
            break
        else:
            print("The code does not exsit!")

print(gamer)


# def gamerCombat(gamer1, gamer2):




