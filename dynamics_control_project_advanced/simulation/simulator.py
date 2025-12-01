
import numpy as np
from core.integrators import euler_step, rk4_step

class Simulator:
    def __init__(self, system, controller=None, observer=None):
        self.system = system
        self.controller = controller
        self.observer = observer

    def run(self, x0, dt, tf, reference=0.0, integrator='euler', noise=None, disturbance=None):
        t = 0.0
        state = np.array(x0, dtype=float)
        history = {'t': [], 'state': [], 'u': [], 'y': []}

        while t <= tf:
            error = reference - state[0] if hasattr(self.controller, 'compute') else 0.0
            u = self.controller.compute(error, dt) if self.controller else 0.0
            if disturbance is not None:
                u += disturbance(t)
            if integrator=='euler':
                state = euler_step(self.system.dynamics, t, state, u, dt)
            else:
                state = rk4_step(self.system.dynamics, t, state, u, dt)

            y = state.copy()
            if noise is not None:
                y += noise(t)

            if self.observer:
                self.observer.predict(u)
                self.observer.update(y)

            t += dt
            history['t'].append(t)
            history['state'].append(state.copy())
            history['u'].append(u)
            history['y'].append(y.copy())
        return history
