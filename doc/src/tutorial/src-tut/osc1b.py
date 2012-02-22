"""Oscillating pendulum."""

import odesolvers, numpy
from math import sin, pi, sqrt

c = 1
Theta = pi/4

def f(u, t):
    theta, omega = u
    return [omega, -c*sin(theta)]

method = odesolvers.RK4(f)
method.set_initial_condition([Theta, 0])
freq = sqrt(c)      # frequency of oscillations when Theta is small
period = 2*pi/freq  # the period of the oscillations
T = 10*period        # final time
N_per_period = 20   # resolution of one period
N = N_per_period*period
time_points = numpy.linspace(0, T, N+1)

u, t = method.solve(time_points)

theta = u[:,0]
omega = u[:,1]

from matplotlib.pyplot import *
theta_small = Theta*numpy.cos(sqrt(c)*t)
plot(t, theta, 'r-', t, theta_small, 'y-')
legend(['theta', 'small angle approximation'])
savefig('tmp.png')
show()
