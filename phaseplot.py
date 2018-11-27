# im going to recreate figure 2 from the paper
import numpy as np
from ypu_ode import *
import matplotlib.pyplot as plt


def n1(y):
    return -f_y(y) / mu


def n2(y):
    return 1 / beta * (delta_x + lambd - kappa * y)


rane = np.linspace(0, 100, 1000)

fig1 = plt.figure()
sub1 = fig1.add_subplot(111)
sub1.plot(rane, n1(rane), label='n1')
sub1.plot(rane, n2(rane), label='n2')
sub1.set_xlabel('y')
sub1.set_ylabel('p')
fig1.legend()
fig1.tight_layout()
plt.show()
