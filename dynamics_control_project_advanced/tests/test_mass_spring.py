# tests/test_mass_spring.py
import numpy as np
from systems.mass_spring import MassSpringDamper

def test_dynamics():
    system = MassSpringDamper(m=1.0, k=10.0, c=1.0)
    state = np.array([0.0, 0.0])
    t = 0.0
    u = 1.0
    x_dot, x_ddot = system.dynamics(t, state, u)
    assert isinstance(x_dot, float)
    assert isinstance(x_ddot, float)
