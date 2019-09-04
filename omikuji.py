def unsei(i):
    if i == 0:
        return "大吉"
    if i == 1:
        return "吉"
    if i == 2:
        return "凶"

import random

print('今日の運勢は... ' + unsei(random.randint(0, 2)))
