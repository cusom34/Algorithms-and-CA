import matplotlib.pyplot as plt
import random

class Stack:
    
    def __init__(self, mass = []):
        self.mass = mass

    def get_list(self):
        return self.mass

    def top(self):
        return self.mass[-1]        

    def next_to_top(self):
        return self.mass[-2]
    
    def join(self, elem):
        self.mass += [elem]

    def show(self):
        print(self.mass)

    def pop(self):
        self.mass.pop()

def get_cotan(point):
    return -(point[0]-points[0][0])/(point[1]-points[0][1])

def graham(points):
    s = Stack() #стек, куда пихаем вершины
    points.sort()
    points.sort(key=lambda obj: obj[1])
    s.join(points[0])   #добавляем самую левую вершину с наименьшей абсциссой - первая точка

    sorted_points = points[1:]
    sorted_points.sort(key=get_cotan) #сортируем по полярному углу(-котангенс) относительно первой точки
    s.join(sorted_points[0]) #добавляем точку с наименьшим полярным углом

    for i in range(1, len(sorted_points)): #идем по сорт. списку
        u = [s.top()[0] - s.next_to_top()[0], s.top()[1] - s.next_to_top()[1]]
        v = [sorted_points[i][0] - s.top()[0], sorted_points[i][1] - s.top()[1]]
        while not (u[0] * v[1] - u[1] * v[0] >= 0): #пока не левый поворот на последних 3 точках: удаляем последнюю вершину
            s.pop()
            u = [s.top()[0] - s.next_to_top()[0], s.top()[1] - s.next_to_top()[1]]
            v = [sorted_points[i][0] - s.top()[0], sorted_points[i][1] - s.top()[1]]
        s.join(sorted_points[i]) #если поворот левый: добавляем точку в стек

    return s.get_list()

points = [[4,2],[-3,-1],[1,2],[-6,5],[5,3],[-2,1], [-1.4,3.2],[5.1,-1.3]]

x = [elem[0] for elem in points]
y = [elem[1] for elem in points]

shape = graham(points)
print(shape)
shape_x = [elem[0] for elem in shape]
shape_y = [elem[1] for elem in shape]

plt.scatter(x,y)
plt.plot(shape_x + [shape_x[0]], shape_y+ [shape_y[0]])
plt.show()





