from datetime import datetime as dt
from pytz import timezone
from random import choice
from pathlib import Path

weekdays = 'Понедельник Вторник Среда Четверг Пятница \
Субботьа Воскресенье'.split()


def format_letwork(wday=0):
    now = dt.now(timezone('Europe/Moscow'))
    day_index = wday if wday else now.weekday()
    with open(Path('texts', 'letwork.txt'), 'r', encoding='UTF-8') as letwork:
        letworks = letwork.readlines()
        letwork = letworks[0] if day_index not in [5, 6] else letworks[1]
    with open(Path('texts', 'cits.txt'), 'r', encoding='UTF-8') as cits:
        cits = cits.readlines()
        cit = choice([cits[x] for x in range(0, len(cits), 3)])
        author = cits[cits.index(cit) + 1]
    content = letwork.replace('<date>', now.strftime("%d.%m.%Y"))
    content = content.replace('<weekday>', weekdays[day_index])
    content = content.replace('<cit>', cit[4:].strip())
    content = content.replace('<author>', author.strip())
    content = content.replace('\\n', '\n')
    return content
