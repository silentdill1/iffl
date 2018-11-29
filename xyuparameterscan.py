import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import xyu_ode as xyu
import numpy as np
import multiprocessing as mp
import pickle

start, end = (0, 60)
timeline = np.linspace(start, end, 1000)
lambdalist = np.logspace(-6, 1, 1000)


def solvation(lambd):
    for timeend in timeline:
        global start
        result = solve_ivp(lambda t, n: xyu.f(t, n, lambd), (start, timeend), xyu.n0)#, t_eval=np.linspace(start, timeend, 1000))
        print(f'l = {lambd}, tmax = {timeend}')
        if result.y[2][-1] > 10**5 or result.y[0][-1] > 10**5 or result.y[1][-1] > 10**5:
            return result
    return result

if __name__ == '__main__':
    pool = mp.Pool(processes=mp.cpu_count()-2)
    results = pool.map(solvation, lambdalist)

    with open('poolresultswaa.pickle', 'wb') as f:  # pickling the results so i dont have to work them out every time
        pickle.dump(results, f)
        print('results written to poolresultswaa')

