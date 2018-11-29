import matplotlib.pyplot as plt
import pickle
import xyuparameterscan as xyu
import numpy as np

with open('poolresultswaa.pickle', 'rb') as fp:
    results = pickle.load(fp)

print(f'shape of results is: {np.shape(results)}, should be {len(xyu.lambdalist)}')
print(f'type of result object is {type(results)}')

x = [result.y[0][-1] for result in results]# get last x value for each result in results
y = [result.y[1][-1] for result in results]
u = [result.y[2][-1] for result in results]


fig1 = plt.figure()
sub1 = fig1.add_subplot(111)
#sub1.plot(lambdalist, x, label='x')
#sub1.plot(lambdalist, y, label='y')
sub1.plot(xyu.lambdalist, u, label='u')
sub1.set_xlabel('lambda')
sub1.set_ylabel('u(t->inf)')
sub1.set_xscale('log')
sub1.set_yscale('log')

fig1.legend()
fig1.savefig('fourphaseplot.png')
