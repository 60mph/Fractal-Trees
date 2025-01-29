import time
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def L(x, y, angle, length, k, alpha, beta, gamma, n, nmax):
    if n != 0:
        x2 = x + length * math.cos(angle)
        y2 = y + length * math.sin(angle)

        draw_intens = (nmax - n) / nmax
        color = (0.7 - 0.5 * draw_intens, draw_intens, 0.0)
        #color = (0.5 + 0.5 * draw_intens, draw_intens * 0.8 , 0.0)

        plt.plot([x, x2], [y, y2], color=color, linewidth=3 * (1.1 - draw_intens))

        new_length = length / k

        new_angle_left = angle + alpha
        new_angle_right = angle - beta
        new_angle_mid = angle + gamma

        new_angle_mid2 = angle - gamma

        x3_left = x + (2/3) * length * math.cos(angle)
        y3_left = y + (2 / 3) * length * math.sin(angle)
        L(x3_left, y3_left, new_angle_left, new_length, k, alpha, beta, gamma, n - 1, nmax)

        x3_right = x + (1/3) * length * math.cos(angle)
        y3_right = y + (1 / 3) * length * math.sin(angle)
        L(x3_right, y3_right, new_angle_right, new_length, k, alpha, beta, gamma, n - 1, nmax)

        x3_mid = x + length * math.cos(angle)
        y3_mid = y + length * math.sin(angle)
        L(x3_mid, y3_mid, new_angle_mid, new_length, k, alpha, beta, gamma, n - 1, nmax)

        #x3_mid = x1 + length * math.cos(angle)
        #y3_mid = y1 + length * math.sin(angle)
        #draw_fractal_tree(x3_mid, y3_mid, new_angle_mid2, new_length, k, alpha, beta, gamma, depth - 1, max_depth)

    else: return

#plt.ion()

scale = 1
length = 100
k = 1.6
alpha = math.radians(40)
beta = math.radians(25)
gamma = math.radians(10)
n = 1

x0, y0 = -30, -130

plt.figure(figsize=(10, 10))
#plt.axis('off')

"""for i in range (1, 10):
    scale *= 1.5
    n+=1
    plt.clf()
    plt.axis(xmin = -500/scale, xmax = 500/scale, ymax = 500/scale, ymin = -500/scale)
    plt.axis('off')
    L(x0, y0, math.radians(90), length, k, alpha, beta, gamma, n, n)
    plt.pause(0.5)

for i in range (1, 10):
    #plt.axis('on')
    scale /= 1.3
    plt.axis(xmin = -500/scale, xmax = 500/scale, ymax = 500/scale, ymin = -500/scale)
    plt.pause(0.01)"""
L(x0, y0, math.radians(90), length, k, alpha, beta, gamma, 10, 10)
plt.axis('equal')
plt.show()