'''
this program is used to draw supper-oscillations
'''

from math import cos, pi

import matplotlib.pyplot as plt

A0 = 1
A1 = 13295000
A2 = -30802818
A3 = 26581909
A4 = -10836909
A5 = 1762818

ANS = [A0, A1, A2, A3, A4, A5]

# to create a range from -0.02 to 0.02 inclusive
RANGE_X = [i * 0.001 for i in range(-20, 21)]

# the n value for f(x) function for the formula: an*cos(2*pi*n*x)
FX_N = 100


def f(x: float, n: int):
    '''
    returns the sigma for `an*cos(2*pi*n*x)` with due regard of
    `an = ANS[n] if n < len(ANS) else 0`
    '''
    res = 0
    for i in range(n):
        an = ANS[i] if i < len(ANS) else 0
        res += an*cos(2*pi*i*x)
    return res


def f_max(x: float):
    '''
    this function is the highest frequency component of `f(x)`
    '''
    return cos(2*pi*5*x)


fx = [f(i, n=FX_N) for i in RANGE_X]
fmx = [f_max(i) for i in RANGE_X]

# plotting figures of f(x) and f_max(x)
plt.plot(RANGE_X, fx, label='f(x)')
plt.plot([0, 0, 0, 0], [0, 0.5, 1, 1.5],  label='y axis')
plt.plot(RANGE_X, fmx, label='f_max(x)')
plt.plot(RANGE_X, [0 for _ in RANGE_X], label='x axis')

# set labels for main window and shape
plt.title('Superoscillating-Function')
plt.ylabel('f(x)')
plt.xlabel('x')

# limit the ploted shape view
axes = plt.gca()
axes.set_xlim([-0.02, 0.02])
axes.set_ylim([-0.01, 1.5])

# fetch the legend handles and their associated labels
plt.legend()

# display all figures
plt.show()
