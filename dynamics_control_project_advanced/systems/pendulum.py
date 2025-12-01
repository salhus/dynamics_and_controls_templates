import numpy as np

class Pendulum:
    def __init__(self, m=1.0, l=1.0, g=9.81, b=0.1):
        self.m = m
        self.l = l
        self.g = g
        self.b = b

    def dynamics(self, t, state, u):
        theta, theta_dot = state
        theta_ddot = (u - self.b * theta_dot - self.m*self.g*self.l*np.sin(theta)) / (self.m*self.l**2)
        return np.array([theta_dot, theta_ddot])

