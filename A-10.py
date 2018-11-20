# A-10 サイコロ
# 1から6の整数をランダムに出力する dice() 関数を実装
import random


def dice():
    dice_number = [1, 2, 3, 4, 5, 6]
    print(random.choice(dice_number))


dice()