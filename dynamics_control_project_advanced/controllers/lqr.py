
import numpy as np
from scipy.linalg import solve_continuous_are

class LQRController:
    def __init__(self, A, B, Q, R):
        self.K = self._lqr(A, B, Q, R)

    def _lqr(self, A, B, Q, R):
        # Solve continuous-time Algebraic Riccati Equation
        P = solve_continuous_are(A, B, Q, R)
        K = np.linalg.inv(R) @ B.T @ P
        return K

    def compute(self, x, x_ref=None):
        if x_ref is None:
            x_ref = np.zeros_like(x)
        u = -self.K @ (x - x_ref)
        return u
