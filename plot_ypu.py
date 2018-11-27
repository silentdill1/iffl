from ypu_ode import f_y
import matplotlib.pyplot as plt
import numpy as np

# dy/dt as function of h(u/x)=u/x


def f_y2(y):
    return (-y+2)**5+16*y-32


NUMBER_OF_POINTS = 600


def plot_func(func, time_frame, sub_plot):
    time_points = np.linspace(time_frame[0], time_frame[1], NUMBER_OF_POINTS)
    values = [func(t) for t in time_points]
    sub_plot.plot(time_points, values)


fig = plt.figure()
plot = fig.add_subplot(111)
for h in range(0, 1):
    plot_func(lambda y: f_y2(y)+h, (0, 4.5), plot)
    plot_func(lambda y: 0, (0, 5), plot)
fig.savefig('xxx')
plt.show()
