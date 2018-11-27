# im going to recreate figure 2 from the paper
import numpy as np
from ypu_ode import *
import matplotlib.pyplot as plt
from plot_ypu import f_y2


def n1(y):
    return -f_y2(y) / mu

def n1a(y):
    return -f_y(y) / mu

kappa = 1


def n2(y, lambd=1):
    n = 1 / beta * (delta_x + lambd - kappa * y)
    return n


rane = np.linspace(0, 5, 1000)
if __name__ == '__main__':
    fig1 = plt.figure()
    sub1 = fig1.add_subplot(111)
    sub1.plot(rane, n1(rane), label='n1', color='aqua')
    sub1.plot(rane, n2(rane, 1), label='n2, $\lambda = 1$', color='#FF7256')
    sub1.plot(rane, n2(rane, 2), label='n2, $\lambda = 2$', color='#EE6A50')
    sub1.plot(rane, n2(rane, 3), label='n2, $\lambda = 3$', color='#CD5B45')
    # sub1.plot(rane, [delta_x / beta for x in rane], ls='--', label='threshold for death')
    sub1.plot(rane, [1 for x in rane], ls='--', label='threshold for death', color='aquamarine')  # for better vis
    sub1.set_xlabel('y')
    sub1.set_ylabel('p')
    sub1.set_ylim((0, 15))
    sub1.set_xlim((0, 5.3))
    fig1.legend()
    fig1.tight_layout()
    fig1.savefig('phaseplotpnot0.pdf')

    fig2 = plt.figure()
    sub21 = fig2.add_subplot(111)
    sub21.plot(rane, [n1(x) if n1(x) >= 0 else 0 for x in rane], label='n1')
    sub21.plot(rane, np.zeros(len(rane)), label='n2, p=0')
    sub21.set_xlabel('y')
    sub21.set_ylabel('p')
    sub21.set_ylim((-0.5, 15))
    sub21.set_xlim((0, 5.3))
    fig2.legend()
    fig2.tight_layout()
    fig2.savefig('phaseplot0.pdf')
