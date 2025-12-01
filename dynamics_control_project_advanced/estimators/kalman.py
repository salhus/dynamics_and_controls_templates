
import numpy as np

class KalmanFilter:
    def __init__(self, A, B, C, Q, R, P0, x0):
        self.A = A
        self.B = B
        self.C = C
        self.Q = Q
        self.R = R
        self.P = P0
        self.x = x0

    def predict(self, u):
        self.x = self.A @ self.x + self.B @ u
        self.P = self.A @ self.P @ self.A.T + self.Q
        return self.x

    def update(self, y):
        S = self.C @ self.P @ self.C.T + self.R
        K = self.P @ self.C.T @ np.linalg.inv(S)
        self.x = self.x + K @ (y - self.C @ self.x)
        self.P = self.P - K @ self.C @ self.P
        return self.x
