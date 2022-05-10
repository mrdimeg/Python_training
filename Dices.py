from collections import Counter


lst = [(1, 2), (3, 4), (5, 6)]


def calc_dice_scores(lst1):

    def duplicates():
        res = any(dice1 == dice2 for dice1, dice2 in lst)
        return res
    duplicates()

    if duplicates() != True:
        final_list = sum(map(sum, lst))
        return final_list
    else:
        return 0




print(calc_dice_scores(lst1))
