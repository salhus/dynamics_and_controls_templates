"""Run Simulation."""
from .control.pid import PID
from .dynamics.system import MassSpringDamper
from .simulation.plotting import plot_everything
from .simulation.simulator import Simulator
import numpy as np


def main():
    """simulate."""
    system = MassSpringDamper(m=1.0, k=20.0, c=2.0)
    controller = PID(kp=5, ki=5, kd=1000)
    sim = Simulator(system, controller)
    dt=0.0005
    t_final = 2.0

    def reference_func(t):
        """Define a time-dependent reference (e.g., a sine wave)."""
       
        ref = np.sin(5 * 2 * np.pi * t) + np.sin(3 * 2 * np.pi * t)
  
        return ref
    
    def reference_func_derivative(reference=reference_func, dt=dt, tf=t_final):
        """Calculate the derivative of the time-dependent reference at each time step."""
        t = 0
        ref_previous = reference(t)
        d_reference = []
        time = []
        while t < tf:
            t += dt
            ref = reference(t)
            d_ref = (ref - ref_previous) / dt if dt > 0 else 0.0
            d_reference.append(d_ref)
            time.append(t)
            ref_previous = ref
        return time, d_reference
    

    history = sim.run(x0=[0, 0],
                      dt = dt,
                      tf=t_final,
                      reference=reference_func,
                      integration_method='rk4_step')
    # Add reference derivative outputs to history
    time, d_reference = reference_func_derivative()
    history['reference_time'] = time
    history['reference_derivative'] = d_reference
    print('Final state:', history['state'][-1])

    plot_everything(history, system)


if __name__ == '__main__':
    main()
