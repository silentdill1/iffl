# im going to recreate figure 2 from the paper
import numpy as np
from ypu_ode import *
import matplotlib.pyplot as plt
from fy_plot import f_y2


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
    sub1.set_ylim((0, 8))
    sub1.set_xlim((0, 5.3))
    fig1.legend()
    fig1.tight_layout()
    fig1.savefig('phaseplotpnot0.pdf')

    fig2 = plt.figure()
    sub21 = fig2.add_subplot(111)
    sub21.plot(rane, [n1(x) if n1(x) >= 0 else 0 for x in rane], label='n1')
    sub21.plot(rane, np.zeros(len(rane)), label='N_{2a}, p=0', color='#CD5B45')
    sub21.plot([0, 4], [0, 0], 'o', color='green', clip_on=False)
    sub21.plot(2, 0, 'o', color='red')
    sub21.plot(2, 0, '.', color='white')
    # for quiver
    xsmall = 0
    xbig = 4.5
    ysmall = -0.5
    ybig = 5
    # x = np.linspace(0, xbig, 30)
    # z = np.linspace(ysmall, ybig, 30)
    # X, Z = np.meshgrid(x, z)
    # u = mu*Z + f_y2(X)
    # v = Z*(delta_x+lambd-kappa*X-beta*Z)
    # sub21.quiver(X, Z, u, v)
    sub21.set_xlabel('y')
    sub21.set_ylabel('p')
    sub21.set_ylim((ysmall, ybig))
    sub21.set_xlim((xsmall, xbig))
    fig2.legend()
    fig2.tight_layout()
    fig2.savefig('phaseplot0.pdf')
