from ypu_ode import f_y
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
'''
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)
'''

# dy/dt as function of h(u/x)=u/x
H_KRIT1 = 32 + (16 / 5) ** (5 / 4) - 16 * (2 + (16 / 5) ** (1 / 4))
H_KRIT2 = 32 - (16 / 5) ** (5 / 4) - 16 * (2 - (16 / 5) ** (1 / 4))

greyCount = -0.25


def f_y2(y):
    return -(y - 2) ** 5 + 16*(y-2)


NUMBER_OF_POINTS = 600


def plot_func(func, time_frame, sub_plot, title='_nolegend_'):
    global greyCount
    greyCount += 0.25
    time_points = np.linspace(time_frame[0], time_frame[1], NUMBER_OF_POINTS)
    values = [func(t) for t in time_points]
    # return sub_plot.plot(time_points, values, label=title, color=(greyCount, greyCount, greyCount))
    return sub_plot.plot(time_points, values, label=title)


if __name__ == '__main__':
    fig = plt.figure()
    plot = fig.add_subplot(111)
    for h in [0]:  # 30, H_KRIT2,
        plot_func(lambda y: f_y2(y) + h, (0, 4.5), plot)  # title='h = '+str(round(h)
    line = plot_func(lambda y: 0, (0, 5), plot)
    plt.setp(line, color='#000000', linewidth=0.7)
    # plot.set_ylabel('f(y) [a.u.]')
    # plot.set_xlabel('y [a.u.]')
    '''
    r1 = [[0, 's'], [1.984, 'i'], [4, 's']]
    r2 = [[0.67, 'i'], [4.205, 's']]
    r3 = [[4.32, 's']]
    # r = [r1, r2, r3]
    r = [r1]
    init = [True, True]
    for ri in r:
        for x0 in ri:
            if x0[1] == 's':
                if init[0]:
                    plot.plot(x0[0], 0, 'o', color='#378416', label='stable steady state')
                    init[0] = False
                else:
                    plot.plot(x0[0], 0, 'o', color='#378416', label='_nolegend_')
            else:
                if init[1]:
                    plot.plot(x0[0], 0, 'o', color='#931717', label='unstable steady state')
                    plot.plot(x0[0], 0, '.', color='w', label='_nolegend_')
                    init[1] = False
                else:
                    plot.plot(x0[0], 0, 'o', color='#931717', label='_nolegend_')
                    plot.plot(x0[0], 0, '.', color='w', label='_nolegend_')
    fig.legend(bbox_to_anchor=(0.5, 0.35),
               bbox_transform=plt.gcf().transFigure)
    '''
    plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off',
                    right='off', left='off', labelleft='off')
    fig.savefig('fy_new')
    plt.show()

