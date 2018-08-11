#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: basic_game_29605903.py
@time: 2018/08/08
"""


from game_control_29605903 import *


def purchase_process_task1(gamer):
    """ instruct user to purchase units by controlling the gamer object"""
    flag_exit = True
    for i in range(max_round_num):
        while flag_exit:
            unit_code = input(
                "\nplease purchase an unit allocated in the poisition {0}:\n{1} = ARCHER($1)"
                "\n{2} = SOLDIER($1) \n{3} = KNIGHT($1) \n{4} = exit\n"
                    .format(i + 1, UNIT_ARCHER, UNIT_SOLDIER, UNIT_KNIGHT, UNIT_KNIGHT+1))

            if unit_code in code_list:
                # control gamer instance to purchase ans store units in a list.
                gamer.purchase_unit(int(unit_code))
                print(gamer)
                break
            elif unit_code == str(UNIT_KNIGHT + 1):
                # exit
                flag_exit = False
            else:
                print("\nThe unit code does not exist!\n")


def gamers_combat_task1(gamer1: Gamer, gamer2: Gamer):
    """ Control game flow. This is the most important function in this file.
        First of all, check if there are any units survive for each player. If so, continue to judge the result for
        current round. Otherwise end the game.
        If game continue, control the gamer instance to do the result operation and gamer instance would maintain the
        list by itself.
        This function don't need to care about how the result come from. All it needs to do is check the return value fr
        from the function get_result_of_combating in unit class.
    """
    round_count = 1
    print("\n\nBattle records:\n")
    while gamer1.has_units_survive() and gamer2.has_units_survive():
        result = gamer1.current_unit.get_result_of_combating(gamer2.current_unit)
        """ ***Display format:***
            ROUND1: LRR 【SOLDIER】VS PPH 【KNIGHT】
            LRR won this round!
        """
        print("\n")
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
    if not gamer1.has_units_survive():
        if not gamer2.has_units_survive():
            print("********{0} and {1} tied this game!********".format(gamer1.gamer_name,gamer2.gamer_name))
        else:
            print("********{0} won this game!********".format(gamer2.gamer_name))
    else:
        print("********{0} won this game!********".format(gamer1.gamer_name))


def creat_computer_gamer_task1(initial_money):
    """use random values to generate a computer opponent. Only for testing."""
    list_to_purchase = random_int_list(UNIT_ARCHER, UNIT_KNIGHT, max_round_num)
    computer_gamer = Gamer(money=initial_money,gamer_name="computer_gamer")
    for code in list_to_purchase:
        computer_gamer.purchase_unit(code)
    print("\nA computer opponent generated.")
    print(computer_gamer)
    prompt_to_continued("\nIf you want to start the game, please press y.\n", "y")

    return computer_gamer


if __name__ == "__main__":

    max_round_num = 10
    initial_money = 10
    code_list = [str(UNIT_ARCHER), str(UNIT_SOLDIER), str(UNIT_KNIGHT)]

    """ Gamer Class maintains the list of the units. """
    # gamer1 relative setting
    gamer1_name = input("Please enter a player1 name.\n")
    gamer1 = Gamer(money=initial_money, gamer_name=gamer1_name)
    purchase_process_task1(gamer1)
    print("Your purchase has been completed.")
    print(gamer1)

    # gamer2 relative setting
    # This is a line separating player1 and player2 information.
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    gamer2_name = input("Please enter a player2 name:\n")
    gamer2 = Gamer(money=initial_money, gamer_name=gamer2_name)
    purchase_process_task1(gamer2)
    print("\nYour purchase has been completed.")
    print(gamer2)
    prompt_to_continued("\n\nIf you want to start the game, please press y.\n", "y")

    # for testing
    # computer_gamer = creat_computer_gamer_task1(initial_money=initial_money)

    # start controlling game according to the game rules
    gamers_combat_task1(gamer1, gamer2)



