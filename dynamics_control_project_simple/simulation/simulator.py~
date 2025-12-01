"""Simulation Integration."""
import numpy as np


class Simulator:
    """Simulator functions for running the system."""

    def __init__(self, system, controller=None):
        """Initialize system and controller."""
        self.system = system
        self.controller = controller

    def euler_step(self, f, t, state, u, dt):
        """Euler Integration."""
        return state + f(t, state, u) * dt

    def rk4_step(self, f, t, state, u, dt):
        """Runge-Kutta 4th order integration."""
        k1 = f(t, state, u)
        k2 = f(t + dt/2, state + dt*k1/2, u)
        k3 = f(t + dt/2, state + dt*k2/2, u)
        k4 = f(t + dt, state + dt*k3, u)
        return state + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    def run(self, x0, dt, tf, reference, integration_method='rk4_step'):
        """Simulate the system with given integration method."""
        t = 0.0
        state = np.array(x0, dtype=float)
        history = {
            't': [],
            'state': [],
            'u': [],
            'reference_signal': []
        }

        while t <= tf:
            # Compute reference at current time step
            ref = reference(t) if callable(reference) else reference

            # Error and control input
            error = ref - state[0]
            u = self.controller.compute(error, dt) if self.controller else 0.0

            # Select integration method (Euler or RK4)
            if integration_method == 'rk4':
                state = self.rk4_step(self.system.dynamics,
                                      t, state, u, dt)
            else:
                state = self.euler_step(self.system.dynamics,
                                        t, state, u, dt)

            # Log data
            history['t'].append(t)
            history['state'].append(state.copy())
            history['u'].append(u)
            history['reference_signal'].append(ref)

            # Print state for debugging
            print(f't: {t:.4f}, state: {state}')  # Add this line

            # Increment time
            t += dt

        return history
