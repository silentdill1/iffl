# im going to recreate figure 2 from the paper
import numpy as np
from ypu_ode import *
import matplotlib.pyplot as plt
from plot_ypu import f_y2


def n1(y):
    return -f_y2(y) / mu


kappa = 1


def n2(y, lambd=1):
    n = 1 / beta * (delta_x + lambd - kappa * y)
    return n


rane = np.linspace(0, 5, 1000)
if __name__ == '__main__':
    fig1 = plt.figure()
    sub1 = fig1.add_subplot(111)
    sub1.plot(rane, n1(rane), label='n1')
    sub1.plot(rane, n2(rane), label='n2, $\lambda = 1$')
    sub1.plot(rane, n2(rane, 2), label='n2, $\lambda = 2$')
    sub1.plot(rane, n2(rane, 3), label='n2, $\lambda = 3$')
    sub1.plot(rane, [delta_x/beta for x in rane], ls='--', label='threshold for death')
    sub1.set_xlabel('y')
    sub1.set_ylabel('p')
    sub1.set_ylim((0, 15))
    sub1.set_xlim((0, 5.3))
    fig1.legend()
    fig1.tight_layout()

    fig2 = plt.figure()
    sub21 = fig2.add_subplot(111)
    sub1.plot(rane, n1(rane), label='n1, $\lambda = 1$')

    plt.show()
