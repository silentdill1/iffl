import numpy as np

#params
lambd = 0 # wir könnens nicht lambda nennen
delta_x = 1
delta_y = 1
beta = 1
mu = 1
kappa = 1

# initial vals
y0 = 0
p0 = 0
u0 = 0
x0 = [y0, p0, u0]

def f_y(y):


def h_p(p):
    #at first we will use mu* p
    #todo implement function for h_p and a switch parameter
    pi = mu*p
    return pi


def f(t, x):
    """
    our differential equations (3a-c in the paper)

    :param t: time
    :param x: state vector at time t
    :return: dx as list
    """
    yi, pi, ui = x

    dy = h_p(pi) + f_y(yi)
    dp = pi*(delta_x + lambd - kappa * yi - beta * pi)
    du = (lambd - kappa * yi) * ui
    return [dy, dp, du]
