
import numpy as np

def euler_step(f, t, state, u, dt):
    return state + f(t, state, u) * dt

def rk4_step(f, t, state, u, dt):
    k1 = f(t, state, u)
    k2 = f(t + dt/2, state + dt/2 * k1, u)
    k3 = f(t + dt/2, state + dt/2 * k2, u)
    k4 = f(t + dt, state + dt * k3, u)
    return state + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
