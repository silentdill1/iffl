import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import ypu_ode as ypu
import numpy as np

start, end = (0, 60)
result = solve_ivp(ypu.f, (start, end), ypu.x0, t_eval=np.linspace(start, end, 1000))

y = result.y[0]
p = result.y[1]
u = result.y[2]

fig1 = plt.figure()
sub1 = fig1.add_subplot(111)
sub1.plot(result.t, y, label='y')
sub1.plot(result.t, p, label='p')
sub1.plot(result.t, u, label='u')
fig1.legend()
plt.show()