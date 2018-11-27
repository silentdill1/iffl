import numpy as np

# params - cell pops in 10^6 cells
# /day
lambd = 1  # /day
delta_x = 0.1  # /day
delta_y = 0.1  # /day
beta = 1  # /day
mu = 10  # /day
kappa = 10 ** (-5)  # /(day*unit cells)
V = 0.25  # /day
K = 100  # * unit cells
epsilon = 10 ** (-5)  # /(day*unit cells)

# initial vals
y0 = 0
p0 = 0
u0 = 1
x0 = [y0, p0, u0]


def f_y(y):
    """
    autocatalysis term, function from paper
    :param y:
    :return:
    """
    return (V * y ** 2 / (K + y)) - epsilon * y ** 2 - delta_y * y


def h_p(p):
    # at first we will use mu* p
    # todo implement function for h_p and a switch parameter
    pi = mu * p
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
    dp = pi * (delta_x + lambd - kappa*yi - beta*pi)
    du = (lambd - kappa*yi) * ui
    return [dy, dp, du]
