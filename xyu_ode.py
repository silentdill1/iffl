import numpy as np

# params - cell pops in 10^6 cells
# /day
lambde = 0.09  # /day
delta_x = 0.1  # /day
delta_y = 0.1  # /day
beta = 1  # /day
mu = 10  # /day
kappa = 10 ** (-5)  # /(day*unit cells)
V = 0.25  # /day
K = 100  # * unit cells
epsilon = 10 ** (-5)  # /(day*unit cells)

# initial vals
x0 = 1
y0 = 1
u0 = 1
n0 = [x0, y0, u0]


def f_y(y):
    """
    autocatalysis and decay term, function from paper
    :param y:
    :return:
    """
    return (V * y ** 2 / (K + y)) - epsilon * y ** 2 - delta_y * y


def h_p(p, q):
    # at first we will use mu* p
    # todo implement function for h_p and a switch parameter
    pi = mu * p/q
    return pi


def f(t, n, lambd=lambde):
    """
    our differential equations (3a-c in the paper)

    :param t: time
    :param x: state vector at time t
    :param lambd: u growth rate
    :return: dx as list
    """

    xi, yi, ui = n

    dx = -xi*delta_x + beta*ui
    dy = h_p(ui, xi) + f_y(yi)
    du = (lambd - kappa*yi) * ui
    return [dx, dy, du]
