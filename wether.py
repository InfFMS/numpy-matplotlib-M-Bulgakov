# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import random
import matplotlib.pyplot as plt
import numpy as np
temp = [random.randint(-20, 40) for i in range(365)]
sr_temp = 0
hot_day = 0
colds = []
p = 0
cold_count = 0

for i in range(365):
    sr_temp += temp[i]
    if temp[i] > 25:
        hot_day += 1
    if p < 0 and temp[i] < 0:
        cold_count += 1
    else:
        colds.append(cold_count)
        cold_count = 0
    p = temp[i]
sr_temp = sr_temp / 365

max_cold = 0
for i in range(len(colds)):
    if max_cold < colds[i]:
        max_cold = colds[i]
print(round(sr_temp), max_cold, hot_day)

fig = plt.figure(figsize=(8, 8))

ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4])
x1 = np.linspace(1, 365, 365)
y1 = np.array(temp)
ax1.plot(x1, y1,  color="yellow")
ax1.set_title("Температура по дням")

for i in range(365):

    if temp[i] < 0:
        point1 = plt.Circle((i + 1, temp[i]), 0.25, color="cyan")
        ax1.add_patch(point1)

    elif temp[i] > 25:
        point2 = plt.Circle((i + 1, temp[i]), 0.25, color="purple")
        ax1.add_patch(point2)

ax2 = fig.add_axes([0.1,0.03,0.8,0.4])
y2 = np.array(temp)
ax2.hist(y2, 46,color='magenta')
ax2.set_title("Количество дней одной температуры")

plt.show()