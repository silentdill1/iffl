from ypu_ode import f_y
import matplotlib.pyplot as plt
import numpy as np

# dy/dt as function of h(u/x)=u/x
H_KRIT1 = 32 + (16 / 5) ** (5 / 4) - 16 * (2 + (16 / 5) ** (1 / 4))
H_KRIT2 = 32 - (16 / 5) ** (5 / 4) - 16 * (2 - (16 / 5) ** (1 / 4))


def f_y2(y):
    return -(y - 2) ** 5 + 16*(y-2)


NUMBER_OF_POINTS = 600


def plot_func(func, time_frame, sub_plot):
    time_points = np.linspace(time_frame[0], time_frame[1], NUMBER_OF_POINTS)
    values = [func(t) for t in time_points]
    sub_plot.plot(time_points, values)


if __name__ == '__main__':
    fig = plt.figure()
    plot = fig.add_subplot(111)
    for h in [H_KRIT2, 0, 30]:
        plot_func(lambda y: f_y2(y) + h, (0, 4.5), plot)
        plot_func(lambda y: 0, (0, 5), plot)
    r1 = np.roots([-32 + H_KRIT1, 16, 0, 0, 0, -1])
    r2 = np.roots([-32, 16, 0, 0, 0, -1])
    r3 = np.roots([-32 + H_KRIT2, 16, 0, 0, 0, -1])
    r = [r1, r2, r3]
    for ri in r:
        for x0 in ri:
            plot.plot(x0, 0, 'o')
    fig.savefig('xxx')
    plt.show()

