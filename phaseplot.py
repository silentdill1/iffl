# im going to recreate figure 2 from the paper
import numpy as np
from ypu_ode import *
import matplotlib.pyplot as plt
from fy_plot import f_y2

plt.rcParams.update({'axes.labelsize': 'small'})
def n1(y):
    return -f_y2(y) / mu


def n1a(y):
    return -f_y(y) / mu


kappa = 1


def n2(y, lambd=1.):
    n = 1 / beta * (delta_x + lambd - kappa * y)
    return n


rane = np.linspace(0, 5, 1000)
if __name__ == '__main__':
    #full fig
    fig1 = plt.figure()
    sub1 = fig1.add_subplot(111)
    sub1.plot(rane, n1(rane), label='$N_y$', color='aqua')
    sub1.plot(rane, n2(rane, 0.5), label='$N_{p2}$, $\lambda = 0.5$', color='#FF7256')
    sub1.plot(rane, n2(rane, 2), label='$N_{p2}$, $\lambda = 2$', color='#EE6A50')
    sub1.plot(rane, n2(rane, 3), label='$N_{p2}$, $\lambda = 3$', color='#CD5B45')
    sub1.plot(rane, n2(rane, 6), label='$N_{p2}$, $\lambda = 6$', color='brown')
    sub1.plot(rane, np.zeros(len(rane)), label=r'$N_{p1}$, p=0', color='#CD5B45', lw=2)
    sub1.plot([0, 4], [0, 0], 'o', color='green', clip_on=False)
    sub1.plot(2, 0, 'o', color='red')
    sub1.plot(2, 0, '.', color='white')
    # sub1.plot(rane, [delta_x / beta for x in rane], ls='--', label='threshold for death')
    sub1.plot(rane, [1 for x in rane], ls='--', label='threshold for death', color='aquamarine')  # for better vis
    sub1.set_xlabel('y', fontsize=18)
    sub1.set_ylabel('p', fontsize=18)
    sub1.set_ylim((-0.1, 8))
    sub1.set_xlim((0, 5.3))
    fig1.legend()
    fig1.tight_layout()
    fig1.savefig('phaseplotpnot0.png', dpi=900)

    fignth = plt.figure()
    subnth = fignth.add_subplot(111)
    subnth.plot(rane, n1(rane), label='$N_y$', color='aqua')
    subnth.plot(rane, n2(rane, 0.5), label='$N_{p2}$, $\lambda = 0.5$', color='#FF7256')
    subnth.plot(rane, n2(rane, 2), label='$N_{p2}$, $\lambda = 2$', color='#EE6A50')
    subnth.plot(rane, n2(rane, 3), label='$N_{p2}$, $\lambda = 3$', color='#CD5B45')
    subnth.plot(rane, n2(rane, 6), label='$N_{p2}$, $\lambda = 6$', color='brown')
    # snthb1.plot(rane, [delta_x / beta for x in rane], ls='--', label='threshold for death')
    #subnth.plot(rane, [1 for x in rane], ls='--', label='threshold for death', color='aquamarine')  # for better vis
    subnth.set_xlabel('y', fontsize=18)
    subnth.set_ylabel('p', fontsize=18)
    subnth.set_ylim((0, 8))
    subnth.set_xlim((0, 5.3))
    fignth.legend()
    fignth.tight_layout()
    fignth.savefig('phaseplotpnothresh.png', dpi=900)

    #for p = 0
    fig2 = plt.figure()
    sub21 = fig2.add_subplot(111)
    sub21.plot(rane, [n1(x) if n1(x) >= 0 else 0 for x in rane], label=r'$N_y$', color='aqua')
    sub21.plot(rane, np.zeros(len(rane)), label=r'$N_{p1}$, p=0', color='#CD5B45')
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
    sub21.set_xlabel('y', fontsize=18)
    sub21.set_ylabel('p', fontsize=18)
    sub21.set_ylim((ysmall, ybig))
    sub21.set_xlim((xsmall, xbig))
    fig2.legend()
    fig2.tight_layout()
    fig2.savefig('phaseplot0.png', dpi=900)

    justNy = plt.figure()
    ny1 = justNy.add_subplot(111)
    ny1.plot(rane, n1(rane), label='$N_y$', color='aqua')
    ny1.set_xlabel('y', fontsize=18)
    ny1.set_ylabel('p', fontsize=18)
    justNy.legend()
    justNy.tight_layout()
    ny1.set_ylim((ysmall, ybig))
    ny1.set_xlim((xsmall, xbig))
    justNy.savefig('justny.png', dpi=900)

    