# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.

import matplotlib.pyplot as plt
import random
#m = int(input())
m = int(1000)
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
a = 1
c = 0
b = []

for i in range(m):
    pos_c = c
    c = random.randint(1, 6)
    if c == 1:
        one += 1
    elif c == 2:
        two += 1
    elif c == 3:
        three += 1
    elif c == 4:
        four += 1
    elif c == 5:
        five += 1
    else:
        six += 1
    if pos_c == c:
        c += 1
    else:
        b.append(a)
        a = 0

max_c = 0
for i in range(len(b)):
    if b[i] > max_c:
        max_c = b[i]

v = [one, two, three, four, five, six, max_c]
name = ['единиЦы', 'ДвоЙки', 'ТрОйкИ', 'чеТВёРкИ', 'пЯТЁРКи', 'ШеСТеРКи', 'ОдинакОвые']
#ax.set_facecolor()
#plt.gcf('gray')
ax = plt.gca()
ax.set_facecolor('purple')
plt.bar(name, v, color='pink')
plt.title(f'{m} бросков кубика')
plt.show()