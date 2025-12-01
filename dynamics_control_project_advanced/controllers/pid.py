
from dataclasses import dataclass
from core.utils import clamp
import numpy as np


@dataclass
class PID:
    kp: float
    ki: float
    kd: float
    integral: float = 0.0
    prev_error: float = 0.0
    u_min: float = -np.inf
    u_max: float = np.inf

    def compute(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error)/dt if dt>0 else 0.0
        self.prev_error = error
        u = self.kp*error + self.ki*self.integral + self.kd*derivative
        return clamp(u, self.u_min, self.u_max)
