# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pyplot as plt
import numpy
import matplotlib
import numpy as np
fig, ax = plt.subplots()
x1 = int(input())
y1 = int(input())
x=x1-1
y=8-y1
a = np.array([[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],])

#plt.plot(x,y)
plt.imshow(a, cmap = 'Purples_r')
bukvi = ['A','B','C','D','E','F','G','H']
plt.xticks(range(8), labels=[f"{bukvi[i]}" for i in range(0, 8)])
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0,-1)])


for i in range(1,9):
    circle = plt.Circle((8- i, y), 0.2, facecolor='cyan')
    ax.add_patch(circle)
for i in range(1,9):
    circle = plt.Circle((x , 8 - i), 0.2, facecolor='cyan')
    ax.add_patch(circle)
for i in range(1,9):
    circle = plt.Circle(( x -i,y+i ), 0.2,  facecolor='cyan')
    ax.add_patch(circle)
for i in range(1,9):
    circle = plt.Circle(( x +i,y-i ), 0.2, facecolor='cyan')
    ax.add_patch(circle)
for i in range(1,9):
    circle = plt.Circle(( x+i,y+i ), 0.2, facecolor='cyan')
    ax.add_patch(circle)
for i in range(1,9):
    circle = plt.Circle(( x-i,y-i ), 0.2, facecolor='cyan')
    ax.add_patch(circle)

circle = plt.Circle((x, y), 0.3, facecolor='magenta')
ax.add_patch(circle)
plt.show()
