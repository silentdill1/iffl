import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import ypu_ode as ypu
import numpy as np

start, end = (0, 100)
result = solve_ivp(ypu.f, (start, end), ypu.x0, t_eval=np.linspace(start, end, 1000))

y = result.y[0]
p = result.y[1]
u = result.y[2]
