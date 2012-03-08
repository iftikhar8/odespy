def f(u, t):
    return a*u*(1 - u/R)

a=2
R=1E+5
A=1

import odespy
solver = odespy.RK4(f)
solver.set_initial_condition(A)

from numpy import linspace, exp
T = 20  # end of simulation
dt = 0.25
N = int(round(T/dt))
time_points = linspace(0, T, N+1)

tol = 100   # tolerance for termination criterion

def terminate(u, t, step_no):
    """u[step_no] holds (the most recent) solution at t[step_no]."""
    if abs(u[step_no] - R) < tol:
        return True
    else:
        return False

u, t = solver.solve(time_points, terminate)
print 'Final u(t=%g)=%g' % (t[-1], u[-1])

from matplotlib.pyplot import *
plot(t, u, 'r-')
savefig('tmp.png')
show()
