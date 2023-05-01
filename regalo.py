# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

angulo = np.linspace(0, 2*np.pi, 100)
x_tapa_superior = 3 * np.cos(angulo)
y_tapa_superior = 1 * np.sin(angulo)

x_tapa_inferior = 3 * np.cos(angulo[50:99])
y_tapa_inferior = 1 * np.sin(angulo[50:99]) - 3

x_tapa_media = 3 * np.cos(angulo[50:99])
y_tapa_media = 1 * np.sin(angulo[50:99]) - 1.5


def rectangulo_x(v1,v2,v3,v4):
    x1 = np.linspace(v1[0], v2[0], 50)

    x2 = np.linspace(v2[0], v4[0], 50)

    x3 = np.linspace(v4[0], v3[0], 50)

    x4 = np.linspace(v3[0], v1[0], 50)

    x = np.concatenate([x1, x2, x3, x4])
    
    return x


def rectangulo_y(v1,v2,v3,v4):
    y1 = np.linspace(v1[1], v2[1], 50)

    y2 = np.linspace(v2[1], v4[1], 50)

    y3 = np.linspace(v4[1], v3[1], 50)

    y4 = np.linspace(v3[1], v1[1], 50)

    y = np.concatenate([y1, y2, y3, y4])
    
    return y


#plt.plot(x_tapa_superior ,y_tapa_superior, color='blue')
plt.plot(x_tapa_inferior ,y_tapa_inferior, color='blue')

plt.fill(x_tapa_inferior, y_tapa_inferior, color='yellow')

v1 = [3, 0.1]
v2 = [-3, 0.1]
v3 = [3, -3.1]
v4 = [-3, -3.1]
#plt.plot(rectangulo_x(v1,v2,v3,v4),rectangulo_y(v1,v2,v3,v4))
plt.title('feliz cumple (es una torta)')
plt.fill(rectangulo_x(v1,v2,v3,v4),rectangulo_y(v1,v2,v3,v4),'yellow')


plt.plot(x_tapa_media,y_tapa_media, color='blue',label='dale boca')

plt.fill(x_tapa_superior, y_tapa_superior, color='blue')

l = np.linspace(2,-2,38)
i = 0
while i < 38:
    v1 = [l[i],2]
    v3 = [l[i],0]
    i+=1
    v2 = [l[i],2]
    v4 = [l[i],0]
    i+=1
    plt.fill(rectangulo_x(v1,v2,v3,v4),rectangulo_y(v1,v2,v3,v4),'yellow')


#v1 = [2, 2]
#v2 = [1.8,2]
#v3 = [2,0]
#v4 = [1.8, 0]
#plt.fill(rectangulo_x(v1,v2,v3,v4),rectangulo_y(v1,v2,v3,v4),'yellow')

plt.legend(loc='upper left')
plt.axis([-5,5,-5,5])
plt.show()



