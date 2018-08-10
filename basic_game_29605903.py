#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: basic_game_29605903.py
@time: 2018/08/08
"""

import random
#import math


from game_control_29605903 import *

def random_int_list(start, stop, length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def prompt_to_continued(prompt,key):
    while (True):
        string = input(prompt)
        if (string == key):
            break

"""control game flow"""
def gamers_combat(gamer1: Gamer, gamer2: Gamer):
    round_count = 1
    while(gamer1.has_units_survive() and gamer2.has_units_survive()):
        result = gamer1.current_unit.get_result_of_combating(gamer2.current_unit)
        if result == RESULT_LOSE:
            print("ROUND{4}: {0} 【{1}】 VS {2} 【{3}】".format(gamer1.gamer_name,gamer1.current_unit,gamer2.gamer_name,gamer2.current_unit,round_count))
            print("{0} won this round!".format(gamer2.gamer_name))
            gamer1.lose()
            gamer2.win()

        elif result == RESULT_WIN:
            print("ROUND{4}: {0} 【{1}】VS {2} 【{3}】".format(gamer1.gamer_name, gamer1.current_unit, gamer2.gamer_name, gamer2.current_unit,round_count))
            print("{0} won this round!".format(gamer1.gamer_name))
            gamer1.win()
            gamer2.lose()

        elif result == RESULT_TIE:
            print("ROUND{4}: {0} 【{1}】VS {2} 【{3}】".format(gamer1.gamer_name, gamer1.current_unit, gamer2.gamer_name, gamer2.current_unit,round_count))
            print("{0} and {1} tied this round!".format(gamer1.gamer_name,gamer2.gamer_name))
            gamer1.tie()
            gamer2.tie()

        round_count += 1
        # press enter to continued next round
        # prompt_to_continued("If you want to continued next round, please press y\n", "y")


    # There is at least one gamer lost all units
    print("\n\nGame end!")
    print("Final result:")
    if(not gamer1.has_units_survive()):
        if(not gamer2.has_units_survive()):
            print("********{0} {1} tied this game!********".format(gamer1.gamer_name,gamer2.gamer_name))
        else:
            print("********{0} won this game!********".format(gamer2.gamer_name))
    else:
        print("********{0} won this game!********".format(gamer1.gamer_name))



if __name__ == "__main__":

    max_round_num = 10
    initial_money = 10
    code_list = [str(UNIT_ARCHER), str(UNIT_SOLDIER), str(UNIT_KNIGHT)]



    """ Gamer Class maintains the list of the units. """
    player_name = input("Please enter a player name.\n")
    gamer = Gamer(money=initial_money,gamer_name=player_name)

    """ process of purchasing units """
    for i in range(max_round_num):
        print(gamer)
        while (True):
            unit_code = input(
            "please purchase an unit placed in the {0} poisition: {1} for ARCHER($1),"
            "{2} for SOLDIER($1),{3} for KNIGHT($1):\n"
                .format(i + 1, UNIT_ARCHER, UNIT_SOLDIER, UNIT_KNIGHT))

            if unit_code in code_list:
                gamer.purchase_unit(int(unit_code))
                break
            else:
                print("The unit code does not exist!")

    print("Your purchase has been completed.")
    print(gamer)


    """Generate a computer opponent"""
    list_to_purchase = random_int_list(UNIT_ARCHER,UNIT_KNIGHT,max_round_num)
    computer_gamer = Gamer(money=initial_money,gamer_name="computer_gamer")
    for code in list_to_purchase:
        computer_gamer.purchase_unit(code)
    print("\nA computer opponent generated.")
    print(computer_gamer)
    prompt_to_continued("If you want to start the game, please press y.\n", "y")

    # start controlling game according to the rules
    gamers_combat(gamer,computer_gamer)

