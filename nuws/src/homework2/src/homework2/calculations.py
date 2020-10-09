#!/usr/bin/env python3

import sympy
from sympy import symbols, Eq, Function, solve, sqrt
import numpy as np
import matplotlib.pyplot as plt
import math

def calculate_velocity(T_val, H_val, W_val):
    W, H, T, t = symbols(r'W, H, T, t') 

    v = Function(r'v')(t)
    x = Function(r'x')(t)
    y = Function(r'y')(t)
    theta = Function(r'theta')(t)

    x = (W/2)*sympy.sin(2*sympy.pi*t/T) # a function for the component x(t) of the figure-eight trajectory
    y = (H/2)*sympy.sin(4*sympy.pi*t/T) # a function for the component y(t) of the figure-eight trajectory

    # taking a derivative
    xdot = x.diff(t)
    ydot = y.diff(t)

    xddot = xdot.diff(t)
    yddot = ydot.diff(t)


    # from the kinematic equations  xdot = v*cos(theta)
    #                               ydot = v*sin(theta) we get:
    v = sqrt(xdot**2 + ydot**2)
    theta = sympy.atan2(ydot, xdot)

    thetadot = theta.diff(t)        # derivative d/dt of theta(t) 
    omega = thetadot                # defining omega

    v = sympy.simplify(v.subs([(W, W_val), (H, H_val), (T, T_val)]))
    omega = sympy.simplify(omega.subs([(W, W_val), (H, H_val), (T, T_val)]))
    x = sympy.simplify(x.subs([(W, W_val), (H, H_val), (T, T_val)]))
    y = sympy.simplify(y.subs([(W, W_val), (H, H_val), (T, T_val)]))

    return x, y, v, omega

class FigureEight():
    def __init__(self, T_val, H_val, W_val):
        self._x, self._y, self._v, self._omega = calculate_velocity(T_val, H_val, W_val)
        self._t = symbols(r't')

    def get_velocity(self, time_step):
        x = self._x.subs(self._t, time_step)
        y = self._y.subs(self._t, time_step)
        v = self._v.subs(self._t, time_step)
        omega = self._omega.subs(self._t, time_step)
        return x, y, v, omega


# fe = FigureEight(100, 7, 9)

# t = symbols(r't')
# t_values = np.arange(0.0, 100.0, 1)
# x_values = []
# y_values = []
# for i in t_values:
#     x, y, v, omega = fe.get_velocity(i)
#     x_values.append(x)
#     y_values.append(y)


# plt.subplot(211)
# plt.plot(t_values, x_values, 'r--')
# plt.subplot(212)
# plt.plot(t_values, y_values, 'b--')
# plt.subplot(221)
# plt.plot(x_values, y_values, 'g--')
# plt.show()