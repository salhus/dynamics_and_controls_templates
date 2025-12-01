"""PID controller implementation."""

from dataclasses import dataclass


@dataclass
class PID:
    """PID controller with proportional, integral, derivative terms."""

    kp: float
    ki: float
    kd: float

    integral: float = 0.0
    prev_error: float = 0.0
    derivative: float = 0.0

    def compute(self, error: float, dt: float) -> float:
        """Compute the PID output given the current error and timestep."""

        # Integral term
        self.integral += error * dt

        # Derivative term (instantaneous)
        self.derivative = (error - self.prev_error) / dt if dt > 0 else 0.0

        # Save for next timestep
        self.prev_error = error

        # PID output
        return (
            self.kp * error
            + self.ki * self.integral
            + self.kd * self.derivative
        )
