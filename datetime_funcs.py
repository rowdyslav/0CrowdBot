from datetime import datetime as dt, timedelta
from pytz import timezone
from random import choice
from pathlib import Path

weekdays = 'Понедельник Вторник Среда Четверг Пятница \
Суббота Воскресенье'.split()


def format_letwork():
    wday = dt.now(timezone('Europe/Moscow')).weekday()
    with open(Path('texts', 'letwork.txt'), 'r', encoding='UTF-8') as letwork:
        letworks = letwork.readlines()
        letwork = letworks[0] if wday not in [5, 6] else letworks[1]
    with open(Path('texts', 'cits.txt'), 'r', encoding='UTF-8') as cits:
        cits = cits.readlines()
        cit = choice([cits[x] for x in range(0, len(cits), 2)])
        author = cits[cits.index(cit) + 1]
    content = letwork.replace('<date>', dt.now().strftime("%d.%m.%Y"))
    content = content.replace('<weekday>', weekdays[wday])
    content = content.replace('<cit>', cit[cit.find(' '):].strip())
    content = content.replace('<author>', author.strip())
    content = content.replace('\\n', '\n')
    return content


def seconds_left():
    now = dt.now(timezone('Europe/Moscow'))
    target = now.replace(hour=7, minute=0, second=0, microsecond=0)
    if target < now:  # если нужное время уже прошло сегодня
        target += timedelta(days=1)  # переходим на завтрашний день
    diff = (target - now).total_seconds()
    print(f'{target} - {now} = {diff} секунд осталось')
    print(f'Это сообщение отправится в нужное время в {weekdays[target.weekday()]}')
    return diff
