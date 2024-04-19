import math
import matplotlib.pylab as plt
import numpy as np


#对数函数的上升速度
def log_speed():
    x = np.arange(0.05, 3, 0.05)
    y1 = [math.log(a, 1.5) for a in x]
    plt.plot(x, y1, linewidth=2, color = '#007500', label = 'log1.5(x)')
    y2 = [math.log(a, 2) for a in x]
    plt.plot(x, y2, linewidth=2, color = '#9F35FF', label = 'log2(x)')
    y3 = [math.log(a, 3) for a in x]
    plt.plot(x, y3, linewidth=2, color = '#F75000', label = 'log3(x)')
    plt.grid(True)
    plt.show()

#plot 对数函数
def log_show():
    x = [float(i) / 100.0 for i in range(1, 300)]
    y = [math.log(i) for i in x]
    plt.plot(x, y, 'r-', linewidth=3, label='log curve')

    a = [x[20], x[175]]
    b = [y[20], y[175]]
    plt.plot(a, b, 'g-', linewidth=2)
    plt.plot(a, b, 'b*', markersize=15, alpha=0.75)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('log(X)')

    plt.show()


if __name__ == '__main__':
    log_speed()

