# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
from unittest.mock import patch

import matplotlib.pyplot as plt
import numpy
import matplotlib
import numpy as np
fig, ax = plt.subplots()
x = int(input())
y = int(input())
a = np.array([[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],])

#plt.plot(x,y)
plt.imshow(a, cmap = 'hot')
bukvi = ['A','B','C','D','E','F','G','H']
plt.xticks(range(8), labels=[f"{bukvi[i]}" for i in range(0, 8)])
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0,-1)])


for i in range(1,9):
    circle = plt.Circle((8- i, int(8) - y), 0.2, edgecolor='black', facecolor='grey')
    ax.add_patch(circle)
for i in range(1,9):
    circle = plt.Circle((8 -x , 8 - i), 0.2, edgecolor='black', facecolor='grey')
    ax.add_patch(circle)


'''for i in range(1,9):
    circle = plt.Circle((8- i-x, int(8) - i), 0.2, edgecolor='black', facecolor='grey')
    ax.add_patch(circle)'''
for i in range(1,9):
    circle = plt.Circle(( 8-x -i,8-y-i ), 0.2, edgecolor='black', facecolor='yellow')
    ax.add_patch(circle)

circle = plt.Circle((8-x, 8-y), 0.3, edgecolor='black', facecolor='red')
ax.add_patch(circle)
plt.show()

