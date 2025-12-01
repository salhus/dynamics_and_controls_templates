
from dataclasses import dataclass
import numpy as np

@dataclass
class MassSpringDamper:
    m: float
    k: float
    c: float

    def dynamics(self, t, state, u):
        x, x_dot = state
        x_ddot = (u - self.c*x_dot - self.k*x)/self.m
        return np.array([x_dot, x_ddot])
