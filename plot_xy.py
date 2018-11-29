import matplotlib.pyplot as plt
from xy_ode import derivatives, uFuns
from scipy.integrate import solve_ivp
import numpy as np

INITIAL_VALUES = np.array([[1, 1],[2,1]])
NUMBER_OF_POINTS = 10000
TIME_FRAME1 = (0.0, 10.0)
TIME_FRAME2 = (0.0, 200.0)
count = 0

def plot_func(func, time_frame, sub_plot):
    time_points = np.linspace(time_frame[0], time_frame[1], NUMBER_OF_POINTS)
    values = [func(t) for t in time_points]
    sub_plot.plot(time_points, values)


def plot_ode(deriv, time_frame, sub_plots, u_func):
    global count
    time_grid = np.linspace(time_frame[0], time_frame[1], NUMBER_OF_POINTS)
    result = solve_ivp(deriv, time_frame, INITIAL_VALUES[count], t_eval=time_grid, method='LSODA')
    count += 1
    for i, sub_plot in enumerate(sub_plots):
        if i == 0:
            plot_func(u_func, time_frame, sub_plot)
            sub_plot.set_ylabel('u [a.u.]', fontsize=16)
            sub_plot.set_title('u', fontsize=16)
        else:
            sub_plot.plot(result.t, result.y[i-1])
            if i == 1:
                sub_plot.set_ylabel('x [a.u.]', fontsize=16)
                sub_plot.set_title('x', fontsize=16)
            if i == 2:
                sub_plot.set_ylabel('y [a.u.]', fontsize=16)
                sub_plot.set_xlabel('t [a.u.]', fontsize=16)
                sub_plot.set_title('y', fontsize=16)


fig, plots = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=False, figsize=(6, 6))
# plot_ode(derivatives[0], TIME_FRAME1, plots, uFuns[0])  # step function
# plot_ode(derivatives[3], TIME_FRAME1, plots, uFuns[3])  # step function
# plot_ode(derivatives[1], TIME_FRAME2, plots, uFuns[1])  # linear
plot_ode(derivatives[2], TIME_FRAME1, plots, uFuns[2])  # exponential
fig.savefig('xxx')
plt.show()
