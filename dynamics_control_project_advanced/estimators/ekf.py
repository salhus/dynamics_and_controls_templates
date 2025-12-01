
import numpy as np

class EKF:
    def __init__(self, f, h, x0, P0, Q, R):
        self.f = f
        self.h = h
        self.x = x0
        self.P = P0
        self.Q = Q
        self.R = R

    def predict(self, u, dt):
        self.x = self.f(0, self.x, u)*dt + self.x
        F = np.eye(len(self.x))  # approximate Jacobian
        self.P = F @ self.P @ F.T + self.Q
        return self.x

    def update(self, y):
        H = np.eye(len(self.x))  # approximate
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x = self.x + K @ (y - self.x)
        self.P = self.P - K @ H @ self.P
        return self.x
