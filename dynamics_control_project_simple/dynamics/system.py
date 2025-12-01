"""Mass, Spring, Damper System Definition."""
from dataclasses import dataclass
import numpy as np


@dataclass
class MassSpringDamper:
    """Initialize Mass, Spring, Damper variables."""

    m: float
    k: float
    c: float

    def dynamics(self, t: float, state: np.ndarray, u: float) -> np.ndarray:
        r"""M\ddot{x}+c\dot{x}+k{x}=u."""
        x, x_dot = state
        x_ddot = (u - self.c * x_dot - self.k * x) / self.m
        return np.array([x_dot, x_ddot])
