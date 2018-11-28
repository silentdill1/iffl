import numpy as np

lambd = 0  # wir könnens nicht lambda nennen
delta_x = 1
delta_y = 1
beta = 1
mu = 1
kappa = 1
t_event1 = 5
t_event2 = 100


def u1(t):
    if t < t_event1:
        return 1
    else:
        return 2


def u2(t):
    if t < t_event2:
        return 1
    else:
        return 1+t-t_event2


def u3(t):
    if t < t_event1:
        return 1
    else:
        return np.exp(t-t_event1)


def deriv1(t, v):
    x = v[0]
    y = v[1]
    dv_dt = np.zeros(2)
    dv_dt[0] = -x*delta_x + beta*u1(t)
    dv_dt[1] = mu*u1(t)/x - delta_y*y
    return dv_dt


def deriv2(t, v):
    x = v[0]
    y = v[1]
    dv_dt = np.zeros(2)
    dv_dt[0] = -x*delta_x + beta*u2(t)
    dv_dt[1] = mu*u2(t)/x - delta_y*y
    return dv_dt


def deriv3(t, v):
    x = v[0]
    y = v[1]
    dv_dt = np.zeros(2)
    dv_dt[0] = -x * delta_x + beta * u3(t)
    dv_dt[1] = mu * u3(t) / x - delta_y * y
    return dv_dt


derivatives = [deriv1, deriv2, deriv3]
uFuns = [u1, u2, u3]