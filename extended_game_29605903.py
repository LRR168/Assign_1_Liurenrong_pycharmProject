#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:liurenrong
@file: extended_game_29605903.py
@time: 2018/08/10
"""

from game_control_29605903 import *

def purchase_process_task2(gamer):
    """ Instruct user to purchase units by controlling the gamer object"""
    flag_exit = True
    has_one = False
    for i in range(max_round_num):
        while flag_exit:
            """
                please purchase an unit allocated in the poisition 1:
                1 = ARCHER($1)
                2 = SOLDIER($1.75) 
                3 = KNIGHT($2.5) 
                4 = exit
                lrr: $10 left
            """
            money_left_str = ("{}: ${} left.\n".format(gamer.gamer_name, gamer.money)) if not has_one else ""
            unit_code = input(
                "\nplease purchase an unit allocated in the poisition {0}:\n{1} = ARCHER($1)"
                "\n{2} = SOLDIER($1.75) \n{3} = KNIGHT($2.5) \n{4} = exit\n"
                    .format(i + 1, UNIT_ARCHER, UNIT_SOLDIER, UNIT_KNIGHT, UNIT_KNIGHT+1)
                + money_left_str)

            if unit_code in code_list:
                has_one = True
                done = gamer.purchase_unit(int(unit_code))
                if not done:
                    print("Not enough money!")
                else:
                    print(gamer)
                break
            elif unit_code == str(UNIT_KNIGHT + 1):
                # exit
                if has_one:
                    flag_exit = False
                else:
                    print("Not buy anything yet!")
            else:
                print("\nThe unit code does not exist!\n")

    # The rest of money would be used to purchase medics automatically.
    print("Your purchase has been completed.")
    print(gamer)
    print("The left money is converted to medics automatically:\n {} has {} medics.\n"
          .format(gamer.gamer_name, gamer.medics))


def gamers_combat_task2(gamer1, gamer2):
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
            ROUND6: LRR 【KNIGHT(3HP)】VS PPH 【ARCHER(1HP)】
            LRR 【KNIGHT(3HP)】-1HP
            PPH 【ARCHER(1HP)】-3HP
            LRR won this round!
        """
        print("\n")
        if result == RESULT_LOSE:
            print("ROUND{4}: {0} 【{1}】 VS {2} 【{3}】".format(gamer1.gamer_name, gamer1.current_unit, gamer2.gamer_name, gamer2.current_unit, round_count))
            print("{0} 【{1}】-{2}HP\n{3} 【{4}】-{5}HP".format(gamer1.gamer_name, gamer1.current_unit, gamer1.current_unit.current_damage, gamer2.gamer_name, gamer2.current_unit, gamer2.current_unit.current_damage))
            print("{0} won this round!".format(gamer2.gamer_name))
            gamer1.lose()
            gamer2.win()

        elif result == RESULT_WIN:
            print("ROUND{4}: {0} 【{1}】VS {2} 【{3}】".format(gamer1.gamer_name, gamer1.current_unit, gamer2.gamer_name, gamer2.current_unit, round_count))
            print("{0} 【{1}】-{2}HP\n{3} 【{4}】-{5}HP".format(gamer1.gamer_name, gamer1.current_unit, gamer1.current_unit.current_damage, gamer2.gamer_name, gamer2.current_unit, gamer2.current_unit.current_damage))
            print("{0} won this round!".format(gamer1.gamer_name))
            gamer1.win()
            gamer2.lose()

        elif result == RESULT_TIE:
            print("ROUND{4}: {0} 【{1}】VS {2} 【{3}】".format(gamer1.gamer_name, gamer1.current_unit, gamer2.gamer_name, gamer2.current_unit, round_count))
            print("{0} 【{1}】-{2}HP\n{3} 【{4}】-{5}HP".format(gamer1.gamer_name, gamer1.current_unit, gamer1.current_unit.current_damage, gamer2.gamer_name, gamer2.current_unit, gamer2.current_unit.current_damage))
            print("{0} and {1} tied this round!".format(gamer1.gamer_name, gamer2.gamer_name))
            gamer1.tie()
            gamer2.tie()

        else:  # both survive. eg 2 knights encounter.
            print("ROUND{4}: {0} 【{1}】VS {2} 【{3}】".format(gamer1.gamer_name, gamer1.current_unit, gamer2.gamer_name, gamer2.current_unit, round_count))
            print("{0} 【{1}】-{2}HP\n{3} 【{4}】-{5}HP".format(gamer1.gamer_name, gamer1.current_unit, gamer1.current_unit.current_damage, gamer2.gamer_name, gamer2.current_unit, gamer2.current_unit.current_damage))

        round_count += 1
        # press enter to continued next round
        # prompt_to_continued("If you want to continued next round, please press y\n", "y")

    # There is at least one gamer lost all units
    print("\n\nGame end!")
    print("Final result:")
    if not gamer1.has_units_survive():
        if not gamer2.has_units_survive():
            print("********{0} and {1} tied this game!********".format(gamer1.gamer_name, gamer2.gamer_name))
        else:
            print("********{0} won this game!********".format(gamer2.gamer_name))
    else:
        print("********{0} won this game!********".format(gamer1.gamer_name))




def creat_computer_gamer_task2(initial_money):
    """use random values to generate a computer opponent. Only for testing."""
    list_to_purchase = random_int_list(UNIT_ARCHER, UNIT_KNIGHT, max_round_num)
    computer_gamer = ExtendedGamer(money=initial_money, gamer_name="computer_gamer")
    for code in list_to_purchase:
        computer_gamer.purchase_unit(code)
    print("\nA computer opponent generated.")
    print(computer_gamer)
    prompt_to_continued("If you want to start the game, please press y.\n", "y")

    return computer_gamer


if __name__ == "__main__":
    max_round_num = 10
    initial_money = 10
    code_list = [str(UNIT_ARCHER), str(UNIT_SOLDIER), str(UNIT_KNIGHT)]

    """ Gamer Class maintains the list of the units. """
    gamer1_name = input("Please press ENTER to enter a player name:\n")
    gamer1 = ExtendedGamer(money=initial_money, gamer_name=gamer1_name)
    purchase_process_task2(gamer1)

    # gamer2 relative setting
    # This is a line separating player1 and player2 information.
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    gamer2_name = input("Please press ENTER to enter a player2 name:\n")
    gamer2 = ExtendedGamer(money=initial_money, gamer_name=gamer2_name)
    purchase_process_task2(gamer2)

    prompt_to_continued("\n\nIf you want to start the game, please press y.\n", "y")


    # for testing
    # computer_gamer = creat_computer_gamer_task2(initial_money=initial_money)


    # start controlling game according to the rules
    gamers_combat_task2(gamer1, gamer2)



