def unsei(i):
    if i == 0:
        return "大吉"
    if i == 1:
        return "中吉"
    if i == 2:
        return "小吉"
    if i == 3:
        return "吉"
    if i == 4:
        return "半吉"
    if i == 5:
        return "末吉"
    if i == 6:
        return "末小吉"
    if i == 7:
        return "凶"
    if i == 8:
        return "小凶"
    if i == 9:
        return "半凶"
    if i == 10:
        return "末凶"
    if i == 11:
        return "大凶"
    return "くじの範囲を超えた...!!!"

import random

print('今日の運勢は... ' + unsei(random.randint(0, 11)))
